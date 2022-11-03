import cv2
img = cv2.imread("solarImage.jpg")


cv2.putText(img, "sun",(20, 150), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255) )
cv2.putText(img, "mercury",(80, 150), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255) )
cv2.putText(img, "venus",(140, 170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255) )
cv2.putText(img, "earth",(200, 130), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255) )
cv2.putText(img, "mars",(260, 170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255) )
cv2.putText(img, "jupiter",(320, 150), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255) )
cv2.putText(img, "saturn",(380, 130), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255) )
cv2.putText(img, "neptune",(440, 170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255) )
cv2.putText(img, "uranus",(500, 150), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255) )

cv2.imshow("output", img)
print(img)
cv2.waitKey(0)