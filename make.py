#! /usr/bin/env python3

import os
import shutil


ALL_DIR = 'all'
ELEMENT_ROOT_DIR = 'computing_elements'
SIM_TYPE_DIRS = [ 'numerical', 'ideal', 'real' ]
VALID_EXTENSIONS = [ '.asc', '.asy', '.cir', '.lib' ]
OTHER_DIRS = [ 'utils', 'spice' ]


if __name__ == '__main__':
    # Make sure we're running in the right directory
    for dir in SIM_TYPE_DIRS + OTHER_DIRS:
        assert os.path.isdir(os.path.join(ELEMENT_ROOT_DIR, dir)), f'Required directory {dir} does not exist'

    # Copy the computing elements to the current directory
    for dir in SIM_TYPE_DIRS:
        for filename in os.listdir(os.path.join(ELEMENT_ROOT_DIR, dir)):
            name, extension = os.path.splitext(filename)
            if extension not in VALID_EXTENSIONS:
                continue
            new_filename = f'{name}_{dir}{extension}'
            shutil.copy(os.path.join(ELEMENT_ROOT_DIR, dir, filename), os.path.join(ALL_DIR, new_filename))

    # Copy the rest of the files to the current directory
    for dir in OTHER_DIRS:
        for filename in os.listdir(os.path.join(ELEMENT_ROOT_DIR, dir)):
            name, extension = os.path.splitext(filename)
            if extension not in VALID_EXTENSIONS:
                continue
            shutil.copy(os.path.join(ELEMENT_ROOT_DIR, dir, filename), os.path.join(ALL_DIR, filename))
