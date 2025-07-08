import matplotlib.pyplot as plt 
import matplotlib 
matplotlib.use("TKAgg")
import numpy as np 

#f(x)=Acos(Bx−C)+D 

A = 1 
B = 2
c = np.pi/4
D = 1

x = np.linspace(0,2*np.pi,600) # Increase 600 (Total points) for smoother and more accurate graph
y = A * np.cos(B * x -c) +D 
plt.figure(figsize=(10,8))
plt.title("COS WAVE")
plt.plot(x,y,"k")
#plt.plot(x,y,"bo")  # circle marker (best to use when Total points is >= 100)  
plt.xlabel("X - AXIS")
plt.ylabel("Y - AXIS")
plt.grid(True)
plt.show()


