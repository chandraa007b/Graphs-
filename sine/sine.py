import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("TKAgg")
import numpy as np 

# Asin(2πft+ϕ)

# plt.figure(figsize=(10,8))
# A  = 1
# phi = np.pi/4
# f = 2 
# t = np.linspace(0,1,1000)
# sinn = A*np.sin(2*np.pi*f*t+phi)
# plt.plot(t,sinn,"b-")
# plt.grid(True)
# plt.show()

# f(x) = Asin(Bx-C)+D

plt.figure(figsize=(10,8))
A = 1 
B = 2
C = np.pi/4
D = 0.5

x = np.linspace(0,2*np.pi,600) # Increase 600 (Total points) for smoother and more accurate graph
y = np.sin(B*x - C) + D 
plt.title("SINE WAVE")
plt.plot(x,y,"b-")
plt.plot(x,y,"bo")  # circle marker (best to use when Total points is >= 100)  
plt.xlabel("X - AXIS")
plt.ylabel("Y - AXIS")
plt.grid(True)
plt.show()


