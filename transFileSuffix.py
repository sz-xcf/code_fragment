
import sys
import os
import shutil

def take_op_on_dir(path, operate, *operate_args, recursive_flag=False):
    """take operation on target dir, recursively or not"""
    parents = os.listdir(path)
    for parent in parents:
        child = os.path.join(path, parent)
        if os.path.isdir(child):
            if recursive_flag:
                take_op_on_dir(child, operate, *operate_args, recursive_flag=recursive_flag)
            else:
                pass
        else:
            operate(child, *operate_args)

def show_usage():
    print('This script is used for transfering the file suffix, to avoiding cryption')
    print('of files with those suffix in certain environment, where the cp command can')
    print('not work\n')

    print('usage: python transFileFuffix.py [dir_name] -decode/-encode {-r}\n')

    #TODO: use sth likewise parsearg to improve this.

def cp_and_change_suffix(src_filename, src_dir, dst_dir, src_suffix, dst_suffix):
    """
    e.g. cp_and_change_suffix('aaa/bbb/ccc/ddd.py', 'ccc', 'zzz'), then get a file
    named 'aaa/bbb/zzz/ddd.pytxt'
    until now, use the abs path, otherwise it may break down
    """

    if src_dir == dst_dir:
        # if same, will it cause a infinite loop? not sure.
        print('Err: dst_dir must be different from src_dir')
        return

    src_tuple = os.path.splitext(src_filename)
    dst_path = src_tuple[0].replace(src_dir, dst_dir, 1)

    if os.path.splitext(src_filename)[1] == src_suffix:
        dst_filename = dst_path + dst_suffix
    else:
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)

        # I hope this more fast than 'cat' or 'cp'
        # dst_filename = dst_path + src_tuple[1]
        dst_filename = dst_path + dst_suffix
        print('cp: ', src_filename, '--->', dst_filename)
        shutil.copyfile(src_filename, dst_filename)

if __name__ == '__main__':
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        show_usage()
        sys.exit()

    if not os.path.exists(sys.argv[1]):
        print('Path not exist: ', sys.argv[1])
        sys.exit()

    if ((sys.argv[2] != '-decode') and (sys.argv[2] != '-encode')):
        show_usage()
        sys.exit()

    recursive = False
    if (len(sys.argv) == 4):
            if (sys.argv[3] != '-r'):
                show_usage()
                sys.exit()
            else:
                recursive = True

    # take_op_on_path(sys.argv[1], print, recursive_flag=recursive)
    # I need some argparse tool, ...
    # take_op_on_dir(sys.argv[1], cp_and_change_suffix, 
            # 'code_fragment', 'TTTTEST', '.py', '.pytxt', recursive_flag=recursive)
    take_op_on_dir(sys.argv[1], cp_and_change_suffix, 
            'code_fragment', 'TTTTEST', '.py', '.pytxt', recursive_flag=recursive)

