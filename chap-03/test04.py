import cv2

img = cv2.imread("./yorkie.png", cv2.IMREAD_COLOR)

# データの切りだし[top:bottom, left:right]
img_roi = img[135:320, 150:290]

cv2.imshow("img", img)
cv2.imshow("img_roi", img_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
