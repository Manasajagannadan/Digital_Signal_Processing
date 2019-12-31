#generating sine and cos waves using samples varing freuency
print('\n\nBy: MANASA J')
input('\nPress "manu" to Start:-')
import numpy as np
import matplotlib.pyplot as plot
#f1=int(input("enter the values of f1:-"))
#f2=int(input("\nenter the values of f2:-"))
#fs=int(input("\nenter the values of fs:-"))
f1=200
f2=400
fs=1000
#sine wave
time=np.arange(0,30,0.1)
x1=np.sin(2*np.pi*f1/fs*time)
x2=np.cos(2*np.pi*f2/fs*time)
plot.subplot(1,3,1)
plot.plot(time,x1)
plot.title("SINE WAVE")
plot.xlabel("TIME")
plot.ylabel("AMPLITUDE")
plot.subplot(1,3,2)
#cos wave
plot.plot(time,x2)
plot.title("COSINE WAVE")
plot.xlabel("TIME")
plot.ylabel("AMPLITUDE")
#adding both waves
y=x1+x2
plot.subplot(1,3,3)
plot.plot(time,y)
plot.title("ADDED WAVE")
plot.xlabel("TIME")
plot.ylabel("AMPLITUDE")
plot.show()
