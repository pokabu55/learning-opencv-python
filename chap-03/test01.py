import numpy as np
import cv2

width = 200
height = 100
value = 128

# 定義のwidth, height, 画素値=0 で埋めたグレースケール画像の作成
img1 = np.zeros((height, width), np.uint8)

# 定義のwidth, height, 画素値=128 で埋めたグレースケール画像の作成
img2 = np.full((height, width), value, np.uint8)

# 表示ウィンドウ
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

img3 = np.zeros((height, width), np.uint8)

# 何かキーを押すとウィンドウを閉じる
cv2.waitKey(0)
cv2.destroyWindow()
