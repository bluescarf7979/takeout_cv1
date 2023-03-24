#!/usr/bin/python3
import cv2
import cv2 as cv
import numpy as np

cap = cv2.VideoCapture(0)       # 카메라 모듈 사용.

while(1):    
    ret, img_color = cap.read()#   카메라 모듈 연속프레임 읽기
    height, width = img_color.shape[:2]
    img_color_blue = cv.resize(img_color, (width, height), interpolation=cv.INTER_AREA)

    hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)    # BGR을 HSV로 변환해줌

    # define range of blue color in HSV
    lower_blue = np.array([100,100,120])          # 파랑색 범위
    upper_blue = np.array([150,255,255])

    # Threshold the HSV image to get only blue colors
    img_mask = cv2.inRange(hsv, lower_blue, upper_blue)     # 110<->150 Hue(색상) 영역을 지정.
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img_color, img_color, mask=img_mask)      # 흰색 영역에 파랑색 마스크를 씌워줌.
    if img_mask.any()== True:
    	print("hello")
    else:
    	print("world")
    

    cv2.imshow('frame',img_color)       # 원본 영상을 보여줌
    cv2.imshow('Blue', res)           # 마스크 위에 파랑색을 씌운 것을 보여줌.
    
   

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
