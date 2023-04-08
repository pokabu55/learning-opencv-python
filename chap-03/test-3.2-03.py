import cv2
import numpy as np

src1 = cv2.imread("./aloeL.png", cv2.IMREAD_COLOR)
src2 = cv2.imread("./aloeR.png", cv2.IMREAD_COLOR)
org_img = cv2.imread("./yorkie.png", cv2.IMREAD_COLOR)

# src1 への重み
alpha = 0.5
# src2 への重み
beta = 0.5
# それぞれの和に加算するスカラー値
gamma = 0.0

# ピクセルごとに重み付け合成を行う
dst1 = cv2.addWeighted(src1, alpha, src2, beta, gamma)

# ピクセルごとに差分の絶対値を取る
dst2 = cv2.absdiff(src1, src2)

# cv2.copyTo でコピー
mask = np.full(org_img.shape, 255, np.uint8)
cv_copy_img = cv2.copyTo(org_img, mask)

# numpy.ndarray.copy でコピー
numpy_copy_img = org_img.copy()

# 浅いコピー
shallow_copy_img = org_img

# コピー元の左上を塗りつぶす
cv2.rectangle(org_img, (0, 0), (100, 100), (255, 255, 255), thickness=-1)

# ｘ軸を中心に回転
dst3 = cv2.flip(org_img, 0)

# 回転
dst4 = cv2.rotate(org_img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)
cv2.imshow("dst4", dst4)
cv2.imshow("cv_copy_img", cv_copy_img)
cv2.imshow("numpy_copy_img", numpy_copy_img)
cv2.imshow("shallow_copy_img", shallow_copy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
