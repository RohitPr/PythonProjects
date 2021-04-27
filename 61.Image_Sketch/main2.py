import cv2
import numpy as np

img_rgb = cv2.imread("img/orig.jpg")
cv2.imshow("img_rgb", img_rgb)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
cv2.imshow("img_gray", img_gray)


img_gray_inv = 255-img_gray

img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(21, 21), sigmaX=0, sigmaY=0)
cv2.imshow("img_blur", img_blur)


def dodgeNaive(image, mask):
    width, height = image.shape[:2]
    blend = np.zeros((width, height), np.uint8)

    for col in range(width):
        for row in range(height):
            if mask[c, r] == 255:
                blend[c, r] = 255
            else:
                tmp = (image[c, r] << 8) / (255-mask)
                if tmp > 255:
                    tmp = 255
                    blend[c, r] = tmp

    return blend


def dodgeV2(image, mask):
    return cv2.divide(image, 255-mask, scale=256)


def dodge(front, back):
    result = front*255/(255-back)
    result[np.logical_or(result > 255, back == 255)] = 255
    return result.astype('uint8')


'''
def burnV2(image, mask):
	return 255–cv2.divide(255-image, 255-mask, scale=256)
'''
img_blend = dodgeV2(img_gray, img_blur)
cv2.imshow("pencil sketch", img_blend)
cv2.imwrite('img/pencil_sketch.png', img_blend)
cv2.waitKey()
