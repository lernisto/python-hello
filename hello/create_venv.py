#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os


def activate(epath, stage2):
    bin = os.path.join(epath, 'bin')
    python = os.path.join(bin, 'python')
    env = os.environ.copy()

    ove = env.pop('VIRTUAL_ENV', None)
    if ove:
        env['_OLD_VIRTUAL_ENV'] = ove
    env['VIRTUAL_ENV'] = epath

    oph = env.pop('PYTHONHOME', None)
    if oph:
        newenv['_OLD_VIRTUAL_PYTHONHOME'] = oph

    path = env['PATH'].split(os.pathsep)
    if bin not in path:
        path.insert(0, bin)
        env['PATH'] = os.pathsep.join(path)

    print('os.execve({}, {}, {})'.format(python, stage2, env))
    os.execve(python, stage2, env)


def check_venv(epath):
    bin = os.path.join(epath, 'bin')
    python = os.path.join(bin, 'python')
    return os.path.exists(epath)


def create(epath):
    try:
        import virtualenv
        virtualenv.create_environment(epath)
    except ImportError:
        import venv
        try:
            venv.create(epath, symlinks=True, with_pip=True)
        except TypeError:
            venv.create(epath, symlinks=True)
            # XXX deal with missing pip??
            # solution: pip install virtualenv for python3.3


def main(epath, *args):
    if not check_venv(epath):
        create(epath)
    activate(epath, args)


if __name__ == '__main__':
    print(sys.argv)
    main(*sys.argv[1:])
