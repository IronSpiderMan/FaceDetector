import cv2
import os
import numpy

# 人脸的根目录
root = './face/'

def getFacesAndLables():

    # 用于存储人脸数据
    faces = []
    # 用于存储标签数据
    labels = []

    # 获取人脸检测器
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # 获取图片路径
    files = os.listdir(root)

    for file in files:
        # 读取图像
        im = cv2.imread(root + file)
        # 灰度转换
        grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        # 检测人脸
        face = face_detector.detectMultiScale(grey)
        for x, y, w, h in face:
            # 设置标签
            labels.append(int(file.split('.')[0]))

            # 设置人脸数据
            faces.append(grey[y:y+h, x:x+w])

    return faces, labels

# 获取人脸数据和标签
faces, labels = getFacesAndLables()

# 获取训练对象
recognizer = cv2.face.LBPHFaceRecognizer_create()
# 训练数据
recognizer.train(faces, numpy.array(labels))
# 保存训练数据
recognizer.write('./trainer.yml')