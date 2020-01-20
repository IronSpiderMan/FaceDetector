import cv2
# 读取图像
im = cv2.imread('face.jpg')
# 灰度转换
grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# 获取人脸检测器
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# 检测人脸
faces = face_detector.detectMultiScale(grey)
# 遍历检测到的人脸
for x, y, w, h in faces:
    cv2.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('im', im)
    cv2.waitKey(0)
cv2.destroyAllWindows()