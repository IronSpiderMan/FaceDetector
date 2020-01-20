import cv2

# 获取训练对象
recognizer = cv2.face.LBPHFaceRecognizer_create()
# 加载训练数据
recognizer.read('trainer.yml')

# 读取图像
im = cv2.imread('Tony.jpg')
# 灰度转换
grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# 获取人脸检测对象
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# 检测人脸
face = face_detector.detectMultiScale(grey)

for x, y, w, h in face:
    label, confidence = recognizer.predict(grey[y:y+h, x:x+w])

    if confidence <= 60:
        if label < 20:
            print('胡歌')
        elif label > 20:
            print('小罗伯特唐尼')
    else:
        print('未匹配到人脸')