import numpy as np
from matplotlib import pyplot as plt
import math 

class ODESolver:

    def __init__(self,F):
        self.F = F
    
    def set_Inital_Conditions(self,y):
        self.y = y
    
    def solve(self, x, interval_stop, step):
        self.interval_start = x
        self.interval_stop = interval_stop
        self.step = step
        X = []
        Y = []
        X.append(self.interval_start)
        Y.append(self.y)
        while x < interval_stop:
            self.y = self.y + self.advance()
            x = x + step
            X.append(x)
            Y.append(self.y)
        return np.array(X), np.array(Y)

    def advance(self):
        raise NotImplementedError

class RK4(ODESolver):
    def advance(self):
        F,x,y,step = self.F, self.interval_start, self.y, self.step
       
        K0 = step*F(x,y)
        K1 = step*F(x + step/2.0, y + K0/2.0)
        K2 = step*F(x+step/2.0, y+ K1/2.0)
        K3 = step*F(x+step,y+K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6
        

g = 9.81
d = 0.063
m = 0.05
air_density = 1.28
v0 = 25.0
theta = 15.0
omega = 20.0
alpha = (air_density * math.pi * d**2)/ (8 * m)
eta = 0

x = 0.0
xStop = 40
y = np.array([0, v0*math.cos(math.radians(theta)), 1, v0*math.sin(math.radians(theta))])
h = 0.01
        
def F(x,y):
    F = np.zeros(4)
    v = math.sqrt((y[1]**2)+(y[3]**2))
    C_D = 0.508 + (1/(22.064 + 4.196*(v/omega)**(5/2)))**(2/5)
    C_M = (1 / (2.022 + 0.981*(v/omega)))

    F[0] = y[1]
    F[1] = (-C_D*alpha*v*y[1]) + (eta*C_M*alpha*v*(y[3]**2)*y[3])
    F[2] = y[3]
    F[3] = (-g)-(C_D*alpha*v*y[3]) - (eta*C_M*alpha*v*y[1])
    return F  

solver = RK4(F)
solver.set_Inital_Conditions(y)
X, Y = solver.solve(x,xStop,h)
print(Y[:,0])
# np.savetxt("notopspinX.csv",X,delimiter=',')
# np.savetxt("notopspinY.csv",Y,delimiter=',')
plt.plot(Y[:,0], Y[:,2])
plt.show()