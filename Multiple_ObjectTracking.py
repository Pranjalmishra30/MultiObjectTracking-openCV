import cv2

trackers = cv2.MultiTracker_create()

Vs = cv2.VideoCapture('Data/Bruno_goal.mp4')

while True:
    ret,frame = Vs.read()

    if not ret : # Ending of frames/Video
        break

    (success,boxes) = trackers.update(frame)

    for box in boxes:
        (x,y,w,h) = [int(v) for v in box]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('frame',frame)
    var = cv2.waitKey(5)

    if var == ord('s'): #Selecting object
        box = cv2.selectROI("frame", frame, fromCenter=False,
			showCrosshair=True)
        tracker = cv2.TrackerCSRT_create() # choosing CSRT type
        trackers.add(tracker,frame,box) # Multi tracker object


    elif var == ord('q'): # Quit
        break

Vs.release()
cv2.destroyAllWindows()
