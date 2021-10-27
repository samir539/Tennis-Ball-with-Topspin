import numpy as np
import matplotlib.pyplot as plt
import math
#Eulers method
def Integrate_Euler(F,x,y,h,xStop):
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop - x)
        y = y + h*F(x,y)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)

def F(x,y):
    F = np.zeros(4)

    C_D = 0.508 + (1/(22.064 + 4.196*(math.sqrt((y[1]**2)*(y[3]**2))/omega)**(5/2)))**(2/5)
    C_M = (1 / 2.022 + 0.981*(math.sqrt((y[1]**2)*(y[3]**2))/omega))

    F[0] = y[1]
    F[1] = -C_D*alpha*math.sqrt((y[1]**2) * (y[3]**2))*y[1] + eta*C_M*alpha*math.sqrt((y[1]**2)*(y[3]**2))*y[3]
    F[2] = y[3]
    F[3] = -g-C_D*alpha*math.sqrt((y[1]**2)*(y[3]**2))*y[3] - eta*C_M*alpha*math.sqrt((y[1]**2)*(y[3]**2))*y[1]
    return F

g = 9.81
d = 0.063
m = 0.05
air_density = 1.29
v0 = 25.0
theta = 15.0
omega = 20.0
alpha = (air_density * math.pi * d**2)/ (8 * m)
eta = 1.0


x = 0.0
xStop = 40
y = np.array([0, v0*math.cos(math.radians(theta)), 1, v0*math.sin(math.radians(theta))])
h = 0.01

X,Y = Integrate_Euler(F,x,y,h,xStop)
#print(X)
#print(Y[:,0])
plt.plot(Y[:,0],Y[:,2])
plt.show()