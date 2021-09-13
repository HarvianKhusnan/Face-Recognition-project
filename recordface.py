import cv2
wajahDir = 'Face Data'
cam = cv2.VideoCapture(0)
cam.set(3, 640) #WidhtCAM
cam.set(4, 480) #HeightCam
faceDetector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeDetector = cv2.CascadeClassifier("haarcascade_eye.xml")
FaceID = input('Masukkan Nama [Tekan Enter]: ')
print("wait for a sec...") 
Ambildata = 0 
while True:
    retV, frame = cam.read()  
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(abuAbu, 1.3, 5)#frame, scaleFactor
    # for (x, y, w, h) in faces :
    #     frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (225,225,0),2)
    #     namaFile = 'wajah.'+str(FaceID)+'.'+str(Ambildata)+'.jpg'
    #     cv2.imwrite(wajahDir+'/'+namaFile, frame) 
    #     Ambildata += 1
    #     roiAbuAbu = abuAbu[y:y+h, x:x+w]
    #     roiWarna = frame[y:y+h, x:x+w]
    #     eyes = eyeDetector.detectMultiScale(roiAbuAbu)
    #     for (xe, ye, we, he) in eyes :
    #         cv2.rectangle(roiWarna, (xe, ye), (xe+we, ye+he), (0,0,255),1)
    cv2.imshow('webcam',frame)
    #cv2.imshow('webcam 2', abuAbu)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break 
    elif Ambildata > 30:
        break
print('Pengambilan Data selesai....')
cam.release()
cv2.destroyAllWindows()
