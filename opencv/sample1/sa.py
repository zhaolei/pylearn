import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('messi5.jpg',0)
#img = cv2.imread('/home/stone/xp/img/icon/dis_access_720.png',0)
img = cv2.imread('/home/stone/xp/img/avator/20150812_150228.jpg',0)
edges = cv2.Canny(img,200,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
