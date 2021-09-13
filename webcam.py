import cv2
can = cv2.VideoCapture(0)
while True:
    retV, frame = can.read()
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('webcam',frame)
    cv2.imshow('webcam 2', abuAbu)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break 
can.release()
cv2.destroyAllWindows()



