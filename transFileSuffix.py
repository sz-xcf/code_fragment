
# This script is used for transfering the file suffix, to avoiding encryption
# of files with those suffix in certain environment, where the cp command can
# not work for this purpose

# e.g.
# python transFileSuffix.py --src_dir `pwd`/somedir_txt --dst_dir `pwd`/somedir 
# --src_suffix .pytxt --dst_suffix .py --recursive --take_action #--ignore_other

import sys
import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--src_dir", type=str, default='', help='the dir which you want to copy from')
parser.add_argument("--dst_dir", type=str, default='', help='the dir which you want copy to')
parser.add_argument("--src_suffix", type=str, default='', help='the suffix you want modify from while copying')
parser.add_argument("--dst_suffix", type=str, default='', help='the suffix you want modify to while copying')
parser.add_argument("--take_action", action='store_true', default=False, help='take action, or else only print action')
parser.add_argument("--ignore_other", action='store_true', default=False, help='ignore files not end with the target suffix')
parser.add_argument("--recursive", action='store_true', default=False, help='take action for the dir recursively')

opt = parser.parse_args()
print(opt)

def take_op_on_dir(path, operate, *operate_args, recursive=False):
    """take operation on target dir, recursively or not"""
    parents = os.listdir(path)
    for parent in parents:
        child = os.path.join(path, parent)
        if os.path.isdir(child):
            if recursive:
                take_op_on_dir(child, operate, *operate_args, recursive=recursive)

        else:
            operate(child, *operate_args)


def cp_and_change_suffix(src_filename, src_dir, dst_dir, src_suffix, dst_suffix, ignore_other, take_action=False):
    """
    this operation is dangerous, you'd better print the action first, (set take_action=False)
    and then make sure if you want to take actions.

    until now, use the abs path, relative path has not been tested.
    """

    dst_path = os.path.dirname(src_filename)
    dst_path = dst_path.replace(src_dir, dst_dir, 1)

    if take_action and (not os.path.exists(dst_path)):
        os.makedirs(dst_path)

    src_tuple = os.path.splitext(src_filename)
    dst_filename = src_tuple[0].replace(src_dir, dst_dir, 1)

    if src_tuple[1] == src_suffix:
        dst_filename = dst_filename + dst_suffix
        print('cp: ', src_filename, ' ====> ', dst_filename)
        if take_action:
            # print('take action now')
            shutil.copyfile(src_filename, dst_filename)

    else:
        if ignore_other:
            return

        dst_filename = dst_filename + src_tuple[1]
        # if take op on other file
        print('cp: ', src_filename, ' ----> ', dst_filename)
        if take_action:
            # print('take action now')
            shutil.copyfile(src_filename, dst_filename)



if __name__ == '__main__':

    if not os.path.exists(opt.src_dir):
        print('Err: path not exist: ', opt.src_dir)
        sys.exit()

    if opt.src_dir == opt.dst_dir:
        # if same, will it cause a infinite loop? not sure.
        print('Err: dst_dir must be different from src_dir')
        sys.exit()

    take_op_on_dir(opt.src_dir, cp_and_change_suffix, opt.src_dir, opt.dst_dir, 
            opt.src_suffix, opt.dst_suffix, opt.ignore_other, opt.take_action, recursive = opt.recursive)


