import cv2

# 读取图像
im = cv2.imread('jpg.png')
# 灰度转换
grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# 保存图像
cv2.imwrite('im.png', grey)
# 销毁所有窗口
cv2.destroyAllWindows()