import numpy as np
# 넘파이 -> 수치 해석, 통계에 쓰이는 파이썬 패키지(수학 및 과학 연산에 사용됨)
import cv2

# opencv 를 import
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# cascade classifier 객체 생성
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# cascade classifier 객체 생성
face_cascade.load('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
# 웹캠에서 이미지 가져오기
while True:
    ret, img = cap.read()
    # 웹캠 이미지를 프레임으로 자름
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 이미지를 그레이스케일로 변환
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    """cascadeclassifier의 detectmultiscale함수에 grayscale 이미지를 입력하여 얼굴 검출
        얼굴이 검출될 시에 위치를 리스트로 리턴 (x,y,w,h)와 같은 튜플
        (x,y)는 검출된 얼굴의 좌상단 위치, w,h는 가로, 세로 크기
        gray->검출해야하는 이미지
        1.3->scalefactor , 30%씩 size를 줄여가며 model detection을 찾음
        5->minNeighbors , detected face의 질에 영향을 줌. 값이 높을수록 높은 질, 적은 detection
   """
    for (x, y, w, h) in faces:
        # 얼굴에 사각형을 그리기
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # 얼굴: 이미지 프레임에 (x,y)에서 시작, (x+넓이, y+길이)까지의 사각형을 그림(색 255 0 0, 굵기 2)
        roi_gray = gray[y:y + h, x:x + w]
        # 이미지를 얼굴 크기만큼 잘라서 그레이스케일 이미지 만듬
        roi_color = img[y:y + h, x:x + w]
        # 이미지를 얼굴 크기만큼 잘라서 컬러이미지 만듬
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            # 눈에 사각형 그리기(얼굴 안에 눈 있으므로 중첩for문 사용)
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            # 눈: 이미지 프레임에 (x,y)에서 시작, (x+넓이, y+길이)까지의 사각형을 그림(색 0 255 0, 굵기 2)
    cv2.imshow('img', img)
    # 찾은 이미지 보여주기
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
# 종료
cv2.destroyAllWindows()
