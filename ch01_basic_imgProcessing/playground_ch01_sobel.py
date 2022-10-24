# カメラから取得した画像をビビンしてみる

import cv2
import numpy as np
from scipy.ndimage import filters


cap = cv2.VideoCapture(0)



while cap.isOpened():
    success, image = cap.read()
    image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Sobel微分係数フィルタ
    imx = np.zeros(image1.shape)
    filters.sobel(image1, 1, imx)

    imy = np.zeros(image1.shape)
    filters.sobel(image1, 0, imy)

    magnitude = np.sqrt(imx**2+ imy**2)

    # image2 = image1 - imy
    image2 =  np.sqrt(imx**2 + imy**2)-80

    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mergeImg = np.hstack((magnitude,image2))


    cv2.imshow('MediaPipe Face Mesh',mergeImg)

    if cv2.waitKey(5)& 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()