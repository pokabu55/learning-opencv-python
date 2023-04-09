import numpy as np
import cv2

img = np.array([[0, 1, 2, 3, 4, 5]])

# 最小値
min = img.min()
max = img.max()
mean = img.mean()

print(f"min = {min}, max = {max}, mean = {mean}")

img2 = np.array([[1, 2, 3], [4, 5, 6]])

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img2)

sum = img.sum()
nz_count = cv2.countNonZero(img)

print(f"min_val = {min_val}, min_loc = {min_loc}, max_val = {max_val}, max_loc = {max_loc}")
print(f"sum = {sum}, not0 = {nz_count}")
