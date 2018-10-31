
import scipy.misc as im
import numpy as np

img = im.imread('pics/dotpic.jpg')
gray = np.dot(img[..., :3], [0.299, 0.587, 0.114])
mask = gray > 210

img[:, :, 0][mask] = 255
img[:, :, 1][mask] = 255
img[:, :, 2][mask] = 255

im.imsave('pics/dotpic_masked.jpg', img)


def save_gray_image(numpy_arr, name):
    """
    save gray image
    input: numpy_arr is a numpy array of shape [w, h, 1]
        and the element is in range[0, 1]
    you'd better save it as png image.
    """
    gray_img = numpy_arr[..., 0]
    misc.imsave(name, (gray_img*255).astype(np.uint8))

def get_binary_img(np_arr, threshold):
    binary = np_arr.copy()

    mask0 = (binary_pic < threshold)
    mask1 = (1-mask0).astype(np.bool)
    binary[mask0] = 0
    binary[mask1] = 1
    
    # save_image_L(binary, 'binary.png')

    return binary

