import csv
import numpy as np
from numpy import genfromtxt
from matplotlib import pyplot as plt


topspinY = genfromtxt('topspinY.csv', delimiter=',')
notopspinY = genfromtxt('notopspinY.csv', delimiter=',')
# with open('topspinX.csv', newline='') as csvfile:
#     topspinX = list(csv.reader(csvfile))
# with open('topspinY.csv') as csvfile:
#     topspinY = list(csv.reader(csvfile))
# with open('notopspinX.csv', newline='') as csvfile:
#     notopspinX = list(csv.reader(csvfile))
# with open('notopspinY.csv', newline='') as csvfile:
#     notopspinY = list(csv.reader(csvfile))

# topspinX = np.asarray(topspinX)
# topspinY = np.asarray(topspinY)
# notopspinX = np.asarray(notopspinX)
# notopspinY = np.asarray(notopspinY)
# print(topspinY[:,0])



plt.plot(topspinY[:,0],topspinY[:,2], 'r', label="with topspin")
plt.plot(notopspinY[:,0], notopspinY[:,2], 'g', label="without topspin")
plt.xlabel("Horizontal Displacement (m)")
plt.ylabel("Verticle Displacement (m)")
plt.legend(loc="upper right")
plt.show()
