
from scipy import signal
import cmath
import numpy as np
import matplotlib.pyplot as plt
j=cmath.sqrt(-1)
t = np.linspace(-1, 1, 500)
x=np.sin(2*np.pi*20*t)
N=8
y=[]
n=np.linspace(-np.pi,np.pi,N)
for n in range(0,N):
    sum=0
    for k in range(0,len(x)):
        sum=sum+x[n]*np.exp(-j*2*3.14*k*n)/N
    y.append(sum)
print("\nx[n]:-",x)#x[n]
print("\nx[k]:-",y)#x[k]
print("\nmagnitude:-",np.abs(y))
print("\npharse:-",np.angle(y))
plt.subplot(411)
plt.xlabel("fre")
plt.ylabel("time")
plt.title("sine signal")
plt.plot(t,x)
plt.subplot(412)
plt.xlabel("fre")
plt.ylabel("time")
plt.title("dft signal")
plt.plot(y)
plt.subplot(413)
plt.xlabel("fre")
plt.ylabel("magnitude")
plt.title("magnitude spectrum")
plt.plot(np.abs(y))
plt.subplot(414)
plt.xlabel("phase")
plt.ylabel("magnitude")
plt.title("pharse spectrum")
plt.plot(np.angle(y))
plt.grid()
plt.show()


