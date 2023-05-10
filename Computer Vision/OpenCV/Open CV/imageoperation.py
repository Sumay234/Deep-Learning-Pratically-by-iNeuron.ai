import cv2
import numpy as np

img = cv2.imread("H:\elonmusk.jpeg")

print("Image shape = ",img.shape)
print("No of Pixels = ",img.size)
print("DataType = ",img.dtype)
print("ImageType = ",type(img))

# Now try to split the image: - split into Blue Green and Red
#print(cv2.split(img))
b,g,r = cv2.split(img)

cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)
#cv2.imshow("original",img)

## Now we will merge the image B G R Image into one
mr1 = cv2.merge((r,g,b))
cv2.imshow("rgb",mr1)

mr2 = cv2.merge((g,b,r))
cv2.imshow("gbr", mr2)
cv2.imshow("original",img)




cv2.waitKey(0)
cv2.destroyAllWindows()