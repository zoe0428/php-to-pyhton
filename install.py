import sys
import argparse
import os
import platform

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--os', type=str, default=None)
args = parser.parse_args()
# print(args.os + '1111111111')


def install_backbond():
    if args.os == 'win':
        print('install win back')

    elif args.os =='linx':
        print('install lunx backbond')
        linux_install()
    else:
        print('error')

def linux_install():
    # install php, py , gcc env
    os.system('sudo apt update')
    os.system('sudo apt install sudo apt install gcc g++ openssl libboost-all-dev')
    os.system('sudo apt install php php-dev php-cli php-gd php-mbstring php-xml php-pear phpunit')
    os.system('sudo apt install python python3 python-dev python3-dev libpython3-all-dev')

    # install php composer
    cmd = """php -r "copy('https://install.phpcomposer.com/installer', 'composer-setup.php');"\n"""
    os.system(cmd)
    os.system('sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer')
    #install thrift
    os.system('git clone https://github.com/apache/thrift.git')
    # arrange the path
    os.system('cd /opt/thrift-0.13')
    os.system('./configure --without-go --without-java --without-ruby ')
    os.system('make')
    os.system('sudo make install')



if __name__ == "__main__":
    install_backbond()