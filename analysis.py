"""
This tool is made specifically for analysing recordings of ray traces of radiation from Wilson cloud chamber

Sample_2 has 158240 pixels
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2


#Opening the sample
cap = cv2.VideoCapture('sample_3.mp4')

#To record the number of pixels per frame
number_pi = []

#For creating the time axis
time_v = []
t = 0

#For counting impulses
n_impulses = 0
temp = 0

while(cap.isOpened()):
    try:
        ret, frame = cap.read()

        #Frame resize (just in case)
        #frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        pixels = np.count_nonzero(gray == 250) #50 - states for the average RGB for the sample #1

        #Counting amount of impulses
        if pixels > temp:
            n_impulses += 1
        temp = pixels

        number_pi.append(pixels)
        cv2.imshow('frame', gray)
        time_v.append(t)
        t += 0.04
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except: 
        break

cap.release()
cv2.destroyAllWindows()

str = ("Approximate number of impulses: {0}\n".format(n_impulses))
print(str)

#Plot configuration
plt.plot(time_v, number_pi)
plt.title('Graph')
plt.ylabel('N of white pixels')
plt.xlabel('Time, s')
plt.show()
