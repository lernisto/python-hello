#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import pip

def main(args):
    for cmd in [
        ('install',
        '-r','dev_requirements.txt',
        '-r','test_requirements.txt',
        '-r','requirements.txt',
        '-e','.'),
    ]:
        pip.main(cmd)

    print('exec',args)
    os.execv(args[0],args)

if __name__=='__main__':
    print(sys.argv)
    main(sys.argv[1:])
