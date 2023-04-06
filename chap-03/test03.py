import cv2

img = cv2.imread("./yorkie.png", cv2.IMREAD_COLOR)

print(f"shape = {img.shape}")
print(f"dtype = {img.dtype}")

if len(img.shape) == 3:
    height, width, channels = img.shape[:3]
else:
    height, width = img.shape[:2]
    channels = 1

print(f"width    = {width}")
print(f"height   = {height}")
print(f"channels = {channels}")


img2 = cv2.imread("./yorkie.png", cv2.IMREAD_GRAYSCALE)

print(f"shape = {img2.shape}")
print(f"dtype = {img2.dtype}")
