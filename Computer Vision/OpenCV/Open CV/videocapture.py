import cv2
'''
# Read video 1:
cap = cv2.VideoCapture("J:\Chinmay\_“Leo_Messi_amazing_performance_VS__Tottenham_😻🔥Follow_me_@messitime1_please”_.mp4")
print(cap)

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(700,450))  # Resize the frame
    cv2.imshow("frame",frame)
    k = cv2.waitKey(25)
    if k == ord("q") & 0xFF:   # it will stop the running video
        break
    
cap.release()  # it is use in video 
cv2.destroyAllWindows()
'''


# To convert the video in gray scale:
# Reading video 2:
'''
cap = cv2.VideoCapture("J:\Chinmay\_“Leo_Messi_amazing_performance_VS__Tottenham_😻🔥Follow_me_@messitime1_please”_.mp4")
print(cap)

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(700,450))  # Resize the frame
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow("gray",gray)
    k = cv2.waitKey(25)       # here 25 is the range the playback speed
    if k == ord("q") & 0xFF:   # it will stop the running video
        break
    
cap.release()  # it is use in video 
cv2.destroyAllWindows()
'''

'''
# Capture Video from web camp 
cap = cv2.VideoCapture(0)   # Here 0 mean laptop webcamp and 1 mean external webcamp
print(cap)
while cap.isOpened():
    ret , frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(700,450))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)
        cv2.imshow("gray",gray)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break      
cap.release()
cv2.destroyAllWindows()
'''

# Capture Video from web camp  and save it:
cap = cv2.VideoCapture(0)   # Here 0 mean laptop webcamp and 1 mean external web camp

# To save the video in formate DIVX, MJPG , XVID , X264
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# It contains four parameters: name,codec,fps,resolution
output = cv2.VideoWriter("H:\\output.avi",fourcc,20.0,(640,480))

print(cap)
while cap.isOpened():
    ret , frame = cap.read()
    if ret == True:
        #frame = cv2.resize(frame,(700,450))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)
        cv2.imshow("gray",gray)
        output.write(frame)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break      
cap.release()
output.release()
cv2.destroyAllWindows()
          



