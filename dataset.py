import pathlib
from utils import get_filenames_of_path

root = pathlib.Path(".../Heads")

inputs = get_filenames_of_path(root / 'input')
inputs.sort()


for idx, path in enumerate(inputs):
    old_name = path.stem
    old_extension = path.suffix
    dir = path.parent
    new_name = str(idx).zfill(3) + old_extension
    path.rename(pathlib.Path(dir, new_name))