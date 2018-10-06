#import OpenCV library
import cv2
#import matplotlib library
import matplotlib.pyplot as plt
#importing time library for speed comparisons of both classifiers
import time 
#matplotlib inline
def convertToRGB(img): 
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
