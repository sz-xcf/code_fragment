# lable imgs into classes by moving them into the corresponding class_dirs
# put this script into the dir where the imgs stored in, and run it

import sys
import glob
import os
import cv2
import collections
import numpy as np

class_dirs = ['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'cu']
label_dict_normal = {
        'NO':'c0',
        'PR':'c1',
        'CR':'c2',
        'PL':'c3',
        'CL':'c4',
        'GF':'c5',
        'DK':'c6',
        'GB':'c7',
        'DR':'c8',
        'TA':'c9',
        'UN':'cu'}
# ordered one
label_dict = collections.OrderedDict(sorted(label_dict_normal.items(),key=lambda t:t[1]))

input_size = (640, 480)
label_width = 64
label_height = 32
label_gap_x = 16
label_gap_y = 12
label_base = (5, 5)

label_positions = [label_base, 
        # (label_base[0] + 1*(label_width + label_gap_x), label_base[1]), 
        # (label_base[0] + 2*(label_width + label_gap_x), label_base[1]), 
        # (label_base[0] + 3*(label_width + label_gap_x), label_base[1]), 
        # (label_base[0] + 4*(label_width + label_gap_x), label_base[1]), 
        # (label_base[0] + 5*(label_width + label_gap_x), label_base[1]),
        (label_base[0], label_base[1] + 1*(label_height + label_gap_y)),
        (label_base[0], label_base[1] + 2*(label_height + label_gap_y)),
        (label_base[0], label_base[1] + 3*(label_height + label_gap_y)),
        (label_base[0], label_base[1] + 4*(label_height + label_gap_y)),
        (label_base[0], label_base[1] + 5*(label_height + label_gap_y)),
        (label_base[0], label_base[1] + 6*(label_height + label_gap_y)),
        (label_base[0], label_base[1] + 7*(label_height + label_gap_y)),
        (label_base[0], label_base[1] + 8*(label_height + label_gap_y)),
        (label_base[0], label_base[1] + 9*(label_height + label_gap_y)),
        (label_base[0], label_base[1] + 10*(label_height + label_gap_y))]

labels = []
some_label_clicked = False
file_name = ''
# -----------------------------------------------------------------------------


class rect:
    def __init__(self, left_up_x, left_up_y, right_down_x, right_down_y):
        self.lu_x = left_up_x
        self.lu_y = left_up_y
        self.rd_x = right_down_x
        self.rd_y = right_down_y

        self.width = right_down_x - left_up_x
        self.height = right_down_y - left_up_y

    def contain_point(self, x, y):
        if self.lu_x <= x <= self.rd_x and self.lu_y <= y <= self.rd_y:
            return True
        return False

class label:
    def __init__(self, rect, label_txt):
        self.rect = rect
        self.txt = label_txt

    def clicked_at(self, x, y):
        if self.rect.contain_point(x, y):
            return True
        return False

# draw labels on img:
def get_poly(rect):
    return np.array([[
        [rect[0], rect[1]],
        [rect[0]+label_width, rect[1]],
        [rect[0]+label_width, rect[1]+label_height],
        [rect[0], rect[1]+label_height]
        ]])

def draw_labels_on_img(img, label_positions):
    
    for position in label_positions:
        # img = cv2.rectangle(img, position, (position[0]+label_width, position[1]+label_height), (255, 0, 0), 2)
        poly = get_poly(position)
        cv2.fillPoly(img, poly, (133, 133, 173))

    label_text = list(label_dict.keys())
    for (i, position) in enumerate(label_positions):
        cv2.putText(img, label_text[i], (label_positions[i][0]+10, label_positions[i][1]+label_height-5), cv2.FONT_HERSHEY_COMPLEX, 1, (222, 16, 16), 1)

# this is the labels in the backend, not the one on the image.
# and this is not coupled with the image
def create_inner_labels(label_positions):
    label_text = list(label_dict.keys())
    for (i, position) in enumerate(label_positions):
        a_rect = rect(position[0], position[1], position[0]+label_width, position[1]+label_height)
        labels.append(label(a_rect, label_text[i]))


def on_mouse(event,x,y,flags,param):
    global file_name, some_label_clicked
    if event==cv2.EVENT_LBUTTONUP:
        for label in labels:
            if label.clicked_at(x, y):
                cmd = 'mv ' + file_name + ' ' + label_dict[label.txt] + '\n'
                print(cmd)
                os.system(cmd)
                some_label_clicked = True
                break


def main():

    global file_name, some_label_clicked

    for sub_dir in class_dirs:
        if not os.path.isdir(sub_dir):
            os.mkdir(sub_dir)

    cv2.namedWindow('showImg')
    cv2.setMouseCallback('showImg', on_mouse)
    create_inner_labels(label_positions)
    this_dir = os.getcwd() + '/'

    for f in os.listdir():
        if f.endswith('.jpg'):
            some_label_clicked = False
            image = cv2.imread(this_dir + f)
            draw_labels_on_img(image, label_positions)
            file_name = f

            while some_label_clicked == False:
                cv2.imshow('showImg', image)
                cv2.waitKey(50)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()


