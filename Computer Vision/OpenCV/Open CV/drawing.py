import cv2
import numpy as np

img = cv2.imread("H:\elonmusk.jpeg")
img = cv2.resize(img,(600,700))

# Here line accept 5 parameter (image, starting matrix, ending matrix, color code , thickness)
img = cv2.line(img, (0,0), (200,200), (245,7,31), 8)  # { here (154,92,424) is a color code from online color picker}


# arrowed line
img = cv2.arrowedLine(img, (2,125) ,(255,255) , (255,0,125), 10)


cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()