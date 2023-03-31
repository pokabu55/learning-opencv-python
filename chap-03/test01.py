import numpy as np
import cv2

width = 200
height = 100
value = 128
channels = 3
value3 = (0, 0, 255)  # BGR

# 定義のwidth, height, 画素値=0 で埋めたグレースケール画像の作成
img1 = np.zeros((height, width), np.uint8)

# 定義のwidth, height, 画素値=128 で埋めたグレースケール画像の作成
img2 = np.full((height, width), value, np.uint8)

# 3ch の真っ黒画像
img3 = np.zeros((height, width, channels), np.uint8)

# 3ch 真っ赤画像
img4 = np.full((height, width, channels), value3, np.uint8)

# 表示ウィンドウ
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.imshow("img4", img4)

# 何かキーを押すとウィンドウを閉じる
cv2.waitKey(0)
cv2.destroyWindow()
