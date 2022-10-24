import cv2
import numpy as np
from scipy.ndimage import  filters

"""
読み込んだ画像にがウシアンフィルタをかける
"""

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    image_ori = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # num = 3
    # 意外とリスト内包表記でやると思い
    # images = [filters.gaussian_filter(image1, i*10) for i in range(num)]
        # mergeImgs =np.hstack((images[0], images[1], images[2]))
    # mergeImg = np.vstack((mergeImgs[0],mergeImgs[1] ))

    # i = 10
    # image1 = filters.gaussian_filter(image_ori, i*5)
    # image2 = filters.gaussian_filter(image_ori, i*10)
    image3 = filters.gaussian_filter(image_ori, 10)
    # mergeImg1 = np.hstack((image1,image2,image3))

    cv2.imshow('MediaPipe Face Mesh',image3)

    if cv2.waitKey(5)& 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()