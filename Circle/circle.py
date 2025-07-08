import matplotlib
matplotlib.use("TkAgg") #Alternative for GTK
import matplotlib.pyplot as plt 
import numpy as np

# x^2+y^2=r^2

r = 1
plt.figure(figsize=(8,8))
theta = np.linspace(0,np.pi*2,1000) # Increase 1000 (Total points) for smoother and more accurate graph

coss = r*np.cos(theta)
sinn = r*np.sin(theta)

plt.plot(coss,sinn,"k")
# plt.plot(coss,sinn,"bo") # Points best to use when Total points points is >= 100  
plt.title("CIRCLE")
plt.xlabel("X - AXIS")
plt.ylabel("Y - AXIS")
plt.grid(True)
plt.show()
