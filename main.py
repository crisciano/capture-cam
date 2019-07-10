#library cv2 cam
import cv2
# select which video cam
cap = cv2.VideoCapture(0)

# loop
while True:
    ret, frame = cap.read()
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()