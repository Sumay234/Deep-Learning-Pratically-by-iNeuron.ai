## Here the video will break into the ScreenShot
import cv2

vidcap = cv2.VideoCapture(r"H:\“Womens_player_of_the_year”_🤩#alexiaputellas_#fcbfemeni_#fcbarcelona_#uefa.mp4") ## video will import 
ret , image = vidcap.read() ## video will read
count = 0
while True:
    if ret == True:
        cv2.imwrite("H:\\zpra\\imgN%d.jpg"%count,image) # Here in imgN%d.jpg{(img=name),(N%d=different image differ name),(%count,image = to count a diferent image to give proper name)}
        ret,image = vidcap.read() # to read the data till end
        cv2.imshow("res",image)
        print("img",count)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
            cv2.destroyAllWindows()
            
vidcap.release()
cv2.destroyAllWindows()
            
        
        