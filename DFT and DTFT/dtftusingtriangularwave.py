from scipy import signal
import cmath
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 1, 500)
N=1000
w=np.linspace(-np.pi,np.pi,N)
x = signal.sawtooth(2 * np.pi * 5 * t,0.5)
j=cmath.sqrt(-1)
y=[]
#for w in range(-1000,1000):
for i in range(0,1000):
    sum=0
    for n in range(0,len(x)):
          #print(len(x))
          sum=sum+(x[n]*np.exp(-j*w[i]*n))
    y.append(sum)
#print(y)
plt.subplot(411)
plt.xlabel("time")
plt.ylabel("amp")
plt.title("tra signal")
plt.plot(t,x)
plt.subplot(412)
plt.xlabel("fre")
plt.ylabel("time")
plt.title("dtft signal")
plt.plot(y)
plt.subplot(413)
plt.xlabel("fre")
plt.ylabel("magnitude")
plt.title("magnitude spectrum")
plt.plot(w,np.abs(y))
plt.subplot(414)
plt.xlabel("phase")
plt.ylabel("magnitude")
plt.title("pharse spectrum")
plt.plot(w,np.angle(y))
plt.grid()
plt.show()


