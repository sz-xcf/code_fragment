# split a datasets into 2 dirs, with ratio = len(SUBDIR1)/len(DATA_DIR)

# usage: this DATA_DIR RATION SUBDIR1 SUBDIR2

import sys
import os
import glob
import random

if len(sys.argv) != 5:
    print('USAGE: python3 ', sys.argv[0], 'DATA_DIR RATIO SUBDIR1 SUBDIR2')
    sys.exit()

total_imgs = glob.glob(sys.argv[1] + '/*.jpg')
total_count = len(total_imgs)

target_imgs = random.sample(total_imgs, int(total_count * float(sys.argv[2])))
target_count = len(target_imgs)

supp_imgs = list(set(total_imgs) - set(target_imgs))
supp_count = total_count - target_count
supp_count = len(supp_imgs)

if not os.path.isdir(sys.argv[3]):
    os.makedirs(sys.argv[3])
if not os.path.isdir(sys.argv[4]):
    os.makedirs(sys.argv[4])

print('total', total_count, 'imgs found in: ', sys.argv[1])
print('cp ', target_count, 'imgs to : ', sys.argv[3])
print('cp ', supp_count, 'imgs to : ', sys.argv[4])

print('=============================')

for img in target_imgs:
    cmd = 'cp ' + img + ' ' +  sys.argv[3]
    print(cmd)
    os.system(cmd)

print('=============================')

for img in supp_imgs:
    cmd = 'cp ' + img + ' ' +  sys.argv[4]
    print(cmd)
    os.system(cmd)



