import numpy as np
import cv2

x = np.uint8([250])
y = np.uint8([5])
z = cv2.add(x, y)
print(f"z={z}")

y = np.uint8([10])
z = cv2.add(x, y)

# uint8 の上限値である 255 となる
print(f"z={z}")

z = cv2.subtract(y, x)
# uint8 の下限値である 0 となる
print(f"z={z}")
