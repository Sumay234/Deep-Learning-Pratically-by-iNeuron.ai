import cv2

camera = "http://26.184.247.99:8080/"
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   # Here 0 mean laptop webcamp and 1 mean external web camp
cap.open(camera)
print("check==",cap.isOpened())


# To save the video in formate DIVX, MJPG , XVID , X264
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# It contains four parameters: name,codec,fps,resolution
output = cv2.VideoWriter("H:\\output.avi",fourcc,20.0,(640,480),0)

print(cap)
while cap.isOpened():
    ret , frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(700,450))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)
        #cv2.imshow("gray",gray)
        output.write(frame)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break      
cap.release()
output.release()
cv2.destroyAllWindows()