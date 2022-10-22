import cv2

img1 = cv2.imread('Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/00-puppy.jpg')
img1 = cv2.resize(img1, (720, 400))
while True:
    cv2.imshow('puppy', img1)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
