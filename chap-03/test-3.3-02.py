# 2枚の画像が同じかどうかをチェックする

import cv2
import numpy as np


def is_same_image(img1, img2):
    # 画像のサイズチェックが必要
    # print(f"img1.shape= {img1.shape}")
    if img1.shape != img2.shape:
        return False

    # 差分計算
    diff = cv2.absdiff(img1, img2)

    return cv2.countNonZero(diff) == 0


def main():
    # cv2.countNonZero が１チャンネルの計算しか出来ないため
    img1 = cv2.imread("./aloeL.png", cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread("./aloeR.png", cv2.IMREAD_GRAYSCALE)
    img3 = cv2.imread("./yorkie.png", cv2.IMREAD_GRAYSCALE)

    print(is_same_image(img1, img1))
    print(is_same_image(img1, img2))
    print(is_same_image(img1, img3))


if __name__ == "__main__":
    main()
