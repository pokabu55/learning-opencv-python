import numpy as np
import cv2

# 画像ファイルをカラーで読み込み
img = cv2.imread("yorkie.png", cv2.IMREAD_COLOR)

x = 200
y = 100
channel = 0

# 座標 x,y の画素値を参照
# 座標指定が y,x の順になっている
bgr_val = img[y, x]
print(f"bgr_val({x},{y}) = {bgr_val}")
# 下記の書き方を f を使うことで簡略化できる
print("bgr_val({},{}) = {}".format(x, y, bgr_val))

# x,y の０番目のチャンネルの画素値
# BGR の順に 0,1,2
b_val = img[y, x, channel]
print(f"b_val{x},{y}")
