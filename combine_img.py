import numpy as np
from PIL import Image
import os.path
import sys


ospj = os.path.join

import scipy.misc
# or: import imageio

def num2str_with_width(number, width):
    if number >= 10**width:
        raise Exception("input out of range: {} >= {}".format(number, 10**width))
    if number < 0:
        raise Exception("only positive input allowed")
    format_str = "%0{}d".format(width)
    return format_str%(number)

def complement_num_str_width(num_str, width):
    num = int(num_str)
    num = num2str_with_width(num, width)
    return str(num)

def combine_img(img_ls, _columns, gap, img_dir = '.'):
    length = len(img_ls)
    assert length > 0

    columns = length if length < _columns else _columns
    _rows = length // columns
    rows = _rows if (length % columns == 0) else (_rows + 1)

    im = np.asarray(Image.open( ospj(img_dir,img_ls[0]) ))
    im_shape = im.shape

    out_im = np.zeros((rows * im_shape[0] + (rows + 1)*gap,
        columns * im_shape[1] + (columns + 1)*gap, 3))

    for index, pic in enumerate(img_ls):
        pic_row = index // columns
        pic_col = index % columns
        location = (pic_row*(im_shape[0] + gap) + gap,
                pic_col*(im_shape[1] + gap) + gap)

        im = np.asarray(Image.open( ospj(img_dir, pic) ))
        assert im.shape[0] == im_shape[0] and im.shape[1] == im_shape[1]

        out_im[location[0]:(location[0]+im_shape[0]),
                location[1]:(location[1]+im_shape[1]), :] = im

    return out_im

if len(sys.argv) == 2:
    img_dir = sys.argv[1]
else:
    img_dir = '.'

orig_ls = list(filter(lambda x: x.endswith('.png'), os.listdir(img_dir)))[:32]
img_ls = []
name_dict = {}
for img_name in orig_ls:
    index1 = img_name.rfind('_')
    index2 = img_name.rfind('.')
    num_str = img_name[index1+1:index2]
    new_name = img_name[:index1+1] + complement_num_str_width(num_str, 5) + '.png'
    name_dict[new_name] = img_name
    img_ls.append(new_name)

img_ls.sort()
print(img_ls)
print(name_dict)

new_ls = []
for img_name in img_ls:
    new_ls.append(name_dict[img_name])

combined_img = combine_img(new_ls, 8, 4, img_dir)
scipy.misc.imsave('combined_img.png', combined_img)
# or: imageio.imwrite('xxxx.png', combined_img)


