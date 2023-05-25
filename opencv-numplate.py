import cv2
import pytesseract

frameWidth = 640 # camera frame width
frameHeight = 480 # camera frame height
plateCascade = cv2.CascadeClassifier( #import plate detector from cv2 library
        "/Users/jayantarora/PycharmProjects/OpencvPython/venv/lib/python3.7/site-packages/cv2/data/haarcascade_russian_plate_number.xml")
minArea = 500 # minimum area that rectangle has to be bigger than
color = (255,0,255) # text color
count = 0 # saved scan counter

cap = cv2.VideoCapture(0) # initialize computer camera
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to grey
    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4) # this will find the number plates in the live feeds

    for (x, y, w, h) in numberPlates: # looping through number plates found to display rectangles over number plates
        area = w*h
        if area > minArea: # if area > minArea, it will declare as rectangle and put text on live photo/video
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, "Number Plate", (x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w] # crops our image to the actual number plate
            cv2.imshow("ROI", imgRoi) # shows the actual number plate cropped in the corner of the screen

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("/Users/jayantarora/PycharmProjects/OpencvPython/venv/lib/python3.7/scanned/Noplate_"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved", (150,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count +=1