#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
minimal script to add a user to the unix password database

This is intended for use in minimal container images
(for example python:alpine) and will most definitely
not work if shadow passwords are in use.

It will also not work unless running as root.

"""

from __future__ import print_function

import os
import pwd
import grp
import sys


def newgroup(groupname, gid):
    record = '{}:x:{}:\n'.format(groupname, gid).encode('ascii')
    with open('/etc/group', 'ab') as gf:
        gf.write(record)


def newuser(name, uid, gid, gecos='', home=None, shell='/sbin/nologin'):
    if home is None:
        home = os.path.join('/home', name)
    record = '{}:x:{}:{}:{}:{}:{}\n'.format(
        name, uid, gid, gecos, home, shell).encode('ascii')
    with open('/etc/passwd', 'ab') as gf:
        gf.write(record)


def addnate():
    homedir = os.path.abspath(os.path.dirname(__file__))
    s = os.stat(homedir)
    uid = s.st_uid
    gid = s.st_gid
    name = os.path.basename(homedir) or 'nate'
    try:
        print('name lookup {}'.format(name))
        u = pwd.getpwnam(name)
        if u.pw_uid == uid:
            print('found match. continuing')
            return
        name = 'nate'
        print('no match. using {}'.format(name))
    except KeyError:
        print('not found. using {}'.format(name))
        pass
    try:
        g = grp.getgrgid(gid)
        print('found group {}'.format(g.gr_name))
    except KeyError:
        print('creating group {}'.format(name))
        newgroup(name, gid)
    try:
        u = pwd.getpwuid(s.st_uid)
    except KeyError:
        print('creating user {}'.format(name))
        newuser(name, uid, gid, 'Nate the Pillow Snake', homedir)
        u = pwd.getpwuid(s.st_uid)
    return u


def execas(user, cmd, cwd=None):
    report_ids('whoami')
    env = os.environ.copy()
    if cwd is None:
        cwd = user.pw_dir
    env['HOME'] = user.pw_dir
    env['USER'] = env['LOGNAME'] = user.pw_name
    env['PWD'] = cwd
    os.setgid(user.pw_gid)
    os.setuid(user.pw_uid)
    os.chdir(cwd)
    report_ids('finished demotion')
    os.execvpe(cmd[0], cmd, env)


def report_ids(msg):
    print('uid, gid = {}, {}; {}'.format(os.getuid(), os.getgid(), msg))


if __name__ == '__main__':
    print(sys.argv)
    execas(addnate(),sys.argv[1:])
