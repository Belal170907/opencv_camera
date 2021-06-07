import cv2
import time

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
y, x, ch = frame.shape

print(y, x)

while True:
    ret, frame = cap.read()
    t = time.ctime( time.time() )

    cv2.rectangle(frame, (0,0), (x,y), (0, 0, 255), 3)
    frame = cv2.putText(frame, t, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 1, cv2.LINE_AA)
    cv2.imshow("webcam", frame)
    key = cv2.waitKey(1)
    if(key == 27):
        break

cv2.destroyAllWindows()
cap.release()