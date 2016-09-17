import os
import pwd
import sys


def main(my_args=None):
    if my_args is None:
        my_args = sys.argv[1:]
    user_name, cwd = my_args[:2]
    args = my_args[2:]
    pw_record = pwd.getpwnam(user_name)
    user_name = pw_record.pw_name
    user_home_dir = pw_record.pw_dir
    user_uid = pw_record.pw_uid
    user_gid = pw_record.pw_gid
    env = os.environ.copy()
    env['HOME'] = user_home_dir
    env['LOGNAME'] = user_name
    env['PWD'] = cwd
    env['USER'] = user_name
    report_ids('starting ' + str(args))
    os.setgid(user_gid)
    os.setuid(user_uid)
    os.chdir(cwd)
    report_ids('finished demotion')
    os.execvpe(args[0], args, env)


def report_ids(msg):
    print 'uid, gid = %d, %d; %s' % (os.getuid(), os.getgid(), msg)


if __name__ == '__main__':
    main()
