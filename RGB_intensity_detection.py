import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('1.png',0)
plt.hist(img.ravel(),256,[0,256]); plt.show()