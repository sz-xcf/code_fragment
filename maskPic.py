
import scipy.misc as im
import numpy as np

img = im.imread('pics/dotpic.jpg')
gray = np.dot(img[..., :3], [0.299, 0.587, 0.114])
mask = gray > 210

img[:, :, 0][mask] = 255
img[:, :, 1][mask] = 255
img[:, :, 2][mask] = 255

im.imsave('pics/dotpic_masked.jpg', img)
