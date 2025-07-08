import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib
matplotlib.use("TKAgg")

# f(x) = Atan(Bx-c)+D 
A = 1
B = 2 
C = np.pi/4
D = 2

x = np.linspace(0,2*np.pi,600) # Increase 600 (Total points) for smoother and more accurate graph
y = np.tan(A*np.tan(B*x - C))+D
plt.figure(figsize=(8,6))
plt.plot(x,y,"k")
#plt.plot(x,y,"bo")   # circle marker (best to use when Total points is > 100)
plt.title("TAN WAVE")
plt.xlabel("X - AXIS")
plt.ylabel("Y - AXIS")
plt.grid(True)
plt.show()
