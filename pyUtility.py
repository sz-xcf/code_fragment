

def num2str_with_width(number, width):
    if number >= 10**width:
        raise Exception("input out of range: {} >= {}".format(number, 10**width))
    if number < 0:
        raise Exception("only positive input allowed")
    format_str = "%0{}d".format(width)
    return format_str%(number)


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
