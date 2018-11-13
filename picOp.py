
import scipy.misc as im
import numpy as np

img = im.imread('pics/dotpic.jpg')
gray = np.dot(img[..., :3], [0.299, 0.587, 0.114])
mask = gray > 210

img[:, :, 0][mask] = 255
img[:, :, 1][mask] = 255
img[:, :, 2][mask] = 255

im.imsave('pics/dotpic_masked.jpg', img)

# ---------------------------------------------------------
def save_gray_image(numpy_arr, name):
    """
    save gray image
    input: numpy_arr is a numpy array of shape [w, h, 1]
        and the element is in range[0, 1]
    you'd better save it as png image.
    """
    gray_img = numpy_arr[..., 0]
    misc.imsave(name, (gray_img*255).astype(np.uint8))
# ---------------------------------------------------------

# ---------------------------------------------------------
def get_binary_img(np_arr, threshold):
    binary = np_arr.copy()

    mask0 = (binary_pic < threshold)
    mask1 = (1-mask0).astype(np.bool)
    binary[mask0] = 0
    binary[mask1] = 1
    
    # save_image_L(binary, 'binary.png')

    return binary
# ---------------------------------------------------------

# ---------------------------------------------------------
import cv2 
import os
def get_avi_from_pics(pic_dir, video_name, frame_rate, size):
    pic_list = os.listdir(img_path)
    pic_list.sort()

    videoWriter = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'MJPG'), frame_rate, size) 
    for path in pic_list: 
        print(img_path + '/' + path)
        img = cv2.imread(img_path + '/' + path) 
        # img = cv2.resize(img,(640,480)) 
        videoWriter.write(img)

# img_path = "/home/sonny/datasets/MOT16/test/MOT16-01/img1"
# get_avi_from_pics(img_path, 'test.avi', 30, (1920, 1080))
# ---------------------------------------------------------

# ---------------------------------------------------------
import cv2 
import numpy 
import scipy.misc

def num2str_with_width(number, width):
    if number >= 10**width:
        raise Exception("input out of range: {} >= {}".format(number, 10**width))
    if number < 0:
        raise Exception("only positive input allowed")
    format_str = "%0{}d".format(width)
    return format_str%(number)


video_to_pics(input_video, output_dir):

    cap = cv2.VideoCapture('output_4.avi') 
    count = 1

    while cv2.waitKey(30)!=ord('q'): 
        retval, image = cap.read() 
        cv2.imshow("video", image) 
        # gbr --> rgb
        img = image[...,::-1]
        
        scipy.misc.imsave(path + num2str_with_width(count, 4) + '.jpg', img)
        count += 1
        
    cap.release()


save_path = 'video2pic/'
file_name 'output_4.avi'
video_to_pics(file_name, save_path)
# ---------------------------------------------------------

# ---------------------------------------------------------
def draw_rect(event,x,y,flags,param): 
    global x1, y1, x2, y2, drawing, frame_h, border_line, border_lines

    if event == cv2.EVENT_LBUTTONDOWN: 
        x1, y1 = x, y
        drawing = True 

    elif event == cv2.EVENT_LBUTTONUP: 
        x2, y2 = x, y
        # WARNING: Line works in 'standard' cordinate in my history code
        # line = Line(x1, y1, x2, y2) # this can't work correctly
        line = Line(x1, frame_h - y1, x2, frame_h - y2) # this can't work
        border_line = BorderLine(line, frame_h)

        if len(border_lines) >= 2:
            border_lines.clear()

        border_lines.append(border_line)

        drawing = False 
# ----------------------------------------------------------

# ----------------------------------------------------------
class Line():

    # point a(a1, a2) to point b(b1, b2)
    def __init__(self, a1, a2, b1, b2):

        self.a1 = a1
        self.a2 = a2

        self.b1 = b1
        self.b2 = b2

    # WARNING: this caculation works in 'standard' cordinate
    def cross_with_line(self, other):

        # print('this line: ', (self.a1, self.a2), (self.b1, self.b2))
        # print('that line: ', (other.a1, other.a2), (other.b1, other.b2))
        # me, other, index
        aa1 = other.a1 - self.a1
        aa2 = other.a2 - self.a2
        ab1 = other.b1 - self.a1
        ab2 = other.b2 - self.a2

        ba1 = other.a1 - self.b1
        ba2 = other.a2 - self.b2
        bb1 = other.b1 - self.b1
        bb2 = other.b2 - self.b2

        c1 = (aa1 * ab2 - aa2 * ab1) * (ba1 * bb2 - ba2 * bb1);
        # print("c1 ---------> ", c1)

        if c1 >= 0 :
                # return False
                # add a cross sign, whit indicate the direction of cross
                return (False, False)

        aa1 = self.a1 - other.a1
        aa2 = self.a2 - other.a2
        ba1 = self.b1 - other.a1
        ba2 = self.b2 - other.a2

        ab1 = self.a1 - other.b1
        ab2 = self.a2 - other.b2
        bb1 = self.b1 - other.b1
        bb2 = self.b2 - other.b2

        # c2 = (aa1 * ba2 - aa2 * ba1) * (ab1 * bb2 - ab2 * bb1);
        # add a cross sign, you can choice any one of these four vector products
        cross_sign = aa1 * ba2 - aa2 * ba1
        c2 = cross_sign * (ab1 * bb2 - ab2 * bb1);
        # print("c2 ---------> ", c2)

        if c2 >= 0 :
                return (False, False)
        else:
                return (True, cross_sign > 0) 


