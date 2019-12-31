from scipy import signal
import cmath
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 1, 500)
N=1000
w=np.linspace(-np.pi,np.pi,N)
x=[6,4]
j=cmath.sqrt(-1)
y=[]
for i in range(0,N):
    sum=0
    for n in range(0,len(x)):
          #print(len(x))
          sum=sum+(x[n]*np.exp(-j*w[i]*n))
    y.append(sum)
#print(y)
plt.subplot(311)
plt.xlabel("fre")
plt.ylabel("time")
plt.title("dtft signal")
plt.plot(y)
plt.subplot(312)
plt.xlabel("fre")
plt.ylabel("magnitude")
plt.title("magnitude spectrum")
plt.plot(w,np.abs(y))
plt.subplot(313)
plt.xlabel("phase")
plt.ylabel("magnitude")
plt.title("pharse spectrum")
plt.plot(w,np.angle(y))
plt.grid()
plt.show()

