
import scipy.misc as im
import numpy as np

img = im.imread('pics/dotpic.jpg')
gray = np.dot(img[..., :3], [0.299, 0.587, 0.114])
mask = gray > 210

img[:, :, 0][mask] = 255
img[:, :, 1][mask] = 255
img[:, :, 2][mask] = 255

im.imsave('pics/dotpic_masked.jpg', img)


# we kan mask any numpy arr, for e.g.
# x_train.shape = (10000, 28, 28, 1)
# mask0 = (x_train[0][..., 0] < 0.5)
# mask1 = (1-mask0).astype(np.bool)
# print(mask0)
# print(mask1)

