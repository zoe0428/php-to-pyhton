import pathlib
import numpy as np
import torch
from typing import List
from datasets import ObjectDetectionDataSet
from torchvision.models.detection.transform import GeneralizedRCNNTransform


def get_filenames_of_path(path: List[pathlib.Path], ext: str = '*'):
    """
    Returns a list of files in a directory/path. Uses pathlib.
    """
    filenames = [file for file in path.glob(ext) if file.is_file()]
    return filenames


def collate_double(batch):
    """
    collate function for the ObjectDetectionDataSet.
    Only used by the dataloader.
    """
    x = [sample['x'] for sample in batch]
    y = [sample['y'] for sample in batch]
    x_name = [sample['x_name'] for sample in batch]
    y_name = [sample['y_name'] for sample in batch]
    return x, y, x_name, y_name


def collate_single(batch):
    """
    collate function for the ObjectDetectionDataSetSingle.
    Only used by the dataloader.
    """
    x = [sample['x'] for sample in batch]
    x_name = [sample['x_name'] for sample in batch]
    return x, x_name


def color_mapping_func(labels, mapping):
    """Maps an label (integer or string) to a color"""
    color_list = [mapping[value] for value in labels]
    return color_list


def enable_gui_qt():
    """Performs the magic command %gui qt"""
    from IPython import get_ipython

    ipython = get_ipython()
    ipython.magic('gui qt')


def stats_dataset(dataset: ObjectDetectionDataSet, rcnn_transform: GeneralizedRCNNTransform = False):
    """
    Iterates over the dataset and returns some stats.
    Can be useful to pick the right anchor box sizes.
    """
    from torchvision.ops import box_convert, box_area
    stats = {
        'image_height': [],
        'image_width': [],
        'image_mean': [],
        'image_std': [],
        'boxes_height': [],
        'boxes_width': [],
        'boxes_num': [],
        'boxes_area': []
    }
    for batch in dataset:
        # Batch
        x, y, x_name, y_name = batch['x'], batch['y'], batch['x_name'], batch['y_name']

        # Transform
        if rcnn_transform:
            x, y = rcnn_transform([x], [y])
            x, y = x.tensors, y[0]

        # Image
        stats['image_height'].append(x.shape[-2])
        stats['image_width'].append(x.shape[-1])
        stats['image_mean'].append(x.mean().item())
        stats['image_std'].append(x.std().item())

        # Target
        wh = box_convert(y['boxes'], 'xyxy', 'xywh')[:, -2:]
        stats['boxes_height'].append(wh[:, -2])
        stats['boxes_width'].append(wh[:, -1])
        stats['boxes_num'].append(len(wh))
        stats['boxes_area'].append(box_area(y['boxes']))

    stats['image_height'] = torch.tensor(stats['image_height'], dtype=torch.float)
    stats['image_width'] = torch.tensor(stats['image_width'], dtype=torch.float)
    stats['image_mean'] = torch.tensor(stats['image_mean'], dtype=torch.float)
    stats['image_std'] = torch.tensor(stats['image_std'], dtype=torch.float)
    stats['boxes_height'] = torch.cat(stats['boxes_height'])
    stats['boxes_width'] = torch.cat(stats['boxes_width'])
    stats['boxes_area'] = torch.cat(stats['boxes_area'])
    stats['boxes_num'] = torch.tensor(stats['boxes_num'], dtype=torch.float)

    return stats


def from_file_to_BoundingBox(file_name: pathlib.Path, groundtruth: bool = True):
    """Returns a list of BoundingBox objects from groundtruth or prediction."""
    from metrics.bounding_box import BoundingBox
    from metrics.enumerators import BBFormat, BBType

    file = torch.load(file_name)
    labels = file['labels']
    boxes = file['boxes']
    scores = file['scores'] if not groundtruth else [None] * len(boxes)

    gt = BBType.GROUND_TRUTH if groundtruth else BBType.DETECTED

    return [BoundingBox(image_name=file_name.stem,
                        class_id=l,
                        coordinates=tuple(bb),
                        format=BBFormat.XYX2Y2,
                        bb_type=gt,
                        confidence=s) for bb, l, s in zip(boxes, labels, scores)]


def from_dict_to_BoundingBox(file: dict, name: str, groundtruth: bool = True):
    """Returns list of BoundingBox objects from groundtruth or prediction."""
    from metrics.bounding_box import BoundingBox
    from metrics.enumerators import BBFormat, BBType

    labels = file['labels']
    boxes = file['boxes']
    scores = np.array(file['scores'].cpu()) if not groundtruth else [None] * len(boxes)

    gt = BBType.GROUND_TRUTH if groundtruth else BBType.DETECTED

    return [BoundingBox(image_name=name,
                        class_id=int(l),
                        coordinates=tuple(bb),
                        format=BBFormat.XYX2Y2,
                        bb_type=gt,
                        confidence=s) for bb, l, s in zip(boxes, labels, scores)]


def log_packages_neptune(neptune_logger):
    """Uses the neptunecontrib.api to log the packages of the current python env."""
    from neptunecontrib.api import log_table
    import pandas as pd

    import importlib_metadata

    dists = importlib_metadata.distributions()
    packages = {idx: (dist.metadata['Name'], dist.version) for idx, dist in enumerate(dists)}

    packages_df = pd.DataFrame.from_dict(packages, orient='index', columns=['package', 'version'])

    log_table(name='packages', table=packages_df, experiment=neptune_logger.experiment)


def log_mapping_neptune(mapping: dict, neptune_logger):
    """Uses the neptunecontrib.api to log a class mapping."""
    from neptunecontrib.api import log_table
    import pandas as pd

    mapping_df = pd.DataFrame.from_dict(mapping, orient='index', columns=['class_value'])
    log_table(name='mapping', table=mapping_df, experiment=neptune_logger.experiment)


def log_model_neptune(checkpoint_path: pathlib.Path,
                      save_directory: pathlib.Path,
                      name: str,
                      neptune_logger):
    """Saves the model to disk, uploads it to neptune and removes it again."""
    import os
    checkpoint = torch.load(checkpoint_path)
    model = checkpoint['hyper_parameters']['model']
    torch.save(model.state_dict(), save_directory / name)
    neptune_logger.experiment.set_property('checkpoint_name', checkpoint_path.name)
    neptune_logger.experiment.log_artifact(str(save_directory / name))
    if os.path.isfile(save_directory / name):
        os.remove(save_directory / name)


def log_checkpoint_neptune(checkpoint_path: pathlib.Path, neptune_logger):
    neptune_logger.experiment.set_property('checkpoint_name', checkpoint_path.name)
    neptune_logger.experiment.log_artifact(str(checkpoint_path))