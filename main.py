import cv2
import pyautogui
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(7, 3000)
cap.set(8, 3000)

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)



    for (x, y , w ,h) in faces:
        rect = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255 , 0), 3)
        img1 = cv2.line(img, (214, 0), (214, 480), (255, 0, 0), 1)
        img2 = cv2.line(img, (428, 0), (428, 480), (255, 0, 0), 1)
        img3 = cv2.line(img, (0, 160), (640, 160), (255, 0, 0), 1)
        img4 = cv2.line(img, (0, 320), (640, 320), (255, 0, 0), 1)

        if x < 190:
            pyautogui.press('left')
            time.sleep(0.5)
        elif y < 140:
            pyautogui.press('up')
            time.sleep(0.5)
        elif x+w > 450:
            pyautogui.press('right')
            time.sleep(0.5)
        elif y+h > 450:
            pyautogui.press('down')
            time.sleep(0.5)

    cv2.namedWindow("Window", cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Window', 1080, 720)
    cv2.imshow('Window', img)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()




