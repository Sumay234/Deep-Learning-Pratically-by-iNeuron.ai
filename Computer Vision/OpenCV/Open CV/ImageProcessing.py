import cv2
'''
# To run the imamge same as it is or Color Image:
import cv2
img2 = cv2.imread(r"J:\pic\IMG_20210801_122207.jpg",1)
img2 = cv2.resize(img2,(1280,700))
cv2.imshow('',img2)
print(img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Image Gray Scale:
img3 = cv2.imread(r"J:\pic\IMG_20210801_122207.jpg",0)
img3 = cv2.resize(img3,(800,400))
cv2.imshow("Gray Scale Image",img3)
print(img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
#path = input(r"Enter Your Path: ")
#print("Your Path is",path)

img1 = cv2.imread("J:\mayapur&camera\IMG_20210917_120927.jpg",0)
img1 = cv2.resize(img1,(560,700))
#img1 = cv2.flip(img1,0)
cv2.imshow("Converted images" , img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''


## Image Convert to Gray Sclae and to Save It
img1 = cv2.imread("J:\Photo\sindur khela2022\IMG_5805.JPG",0)
img1 = cv2.resize(img1,(560,700))
img1 = cv2.flip(img1,1)
cv2.imshow("Converted images" , img1)

k = cv2.waitKey(0)  # To save the image after chaning it
if k==ord('s'):
    cv2.imwrite('H:\\output.png',img1)
    print("iMAGE saves in H drive ")
else:
    cv2.destroyAllWindows()