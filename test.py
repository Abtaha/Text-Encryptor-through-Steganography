import cv2
from random import randint

img = cv2.imread("image.png")
txt = list("Hello")
for i in range(5):
    #char = ord(txt[i])
    
    a = img[i][0][1]
    b = img[i][0][2]
    
    
    print(img[a][b][0])
    
    if i == 5:
        break