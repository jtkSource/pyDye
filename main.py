from jtk.di import dye

__author__ = 'jubin'

import sys, os

sys.path.extend(os.getcwd())

if __name__ == '__main__':
    dye.load_di('pydi.yaml')

    s = dye.get_instance('jubin.body')

    s.print()
