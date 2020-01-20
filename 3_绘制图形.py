import cv2
# 读取图像
im = cv2.imread('test.jpg')
# 绘制图形
cv2.rectangle(im, (10, 10), (50, 50), (0, 255, 0), 3)
cv2.circle(im, (100, 100), 50, (0, 0, 255), 2)
# 显示图像
cv2.imshow('im', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
