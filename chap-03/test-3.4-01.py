import cv2

img = cv2.imread("./yorkie.png", cv2.IMREAD_COLOR)

# プレーンの抽出
b_plane, g_plane, r_plane = cv2.split(img)

# こういった書き方も可能
b_chan = img[:, :, 0]
g_chan = img[:, :, 1]
r_chan = img[:, :, 2]

# プレーンの統合
merged = cv2.merge((b_chan, g_chan, r_chan))

# 画像の連結
hconcat_img = cv2.hconcat([b_chan, g_chan])
vconcat_img = cv2.vconcat([b_chan, r_chan])

print(f"img={img.shape}")

cv2.imshow("b_chan", b_plane)
cv2.imshow("b_chan2", b_chan)
cv2.imshow("g_chan", g_plane)
cv2.imshow("g_chan2", g_chan)
cv2.imshow("r_chan", r_plane)
cv2.imshow("r_chan2", r_chan)
cv2.imshow("merged", merged)
cv2.imshow("hconcat_img", hconcat_img)
cv2.imshow("vconcat_img", vconcat_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
