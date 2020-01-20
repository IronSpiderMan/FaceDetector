import cv2

# 读取图片
im = cv2.imread('test.jpg')
# 显示图片
cv2.imshow('img', im)
# 等待键盘输入
cv2.waitKey(0)
# 销毁所有窗口
cv2.destroyAllWindows()