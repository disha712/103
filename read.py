import cv2

img=cv2.imread("poster.jpg")
rocket=img[120:360,400:500]
img[0:240,500:600]=rocket
cv2.putText(img,"Poster",(20,220),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
cv2.imshow("Output",img)
cv2.waitKey(0)