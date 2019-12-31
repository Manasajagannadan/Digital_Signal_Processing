#generating cos&sine wave
print('\n\nBy: MANASA J')
input('\nPress "manu" to Start:-')
import numpy as np
import matplotlib.pyplot as plot
#giving the time values using linespace
#linspace:-linspace is the numerical method used in matpltlib
time=np.linspace(0,10,80)
#time=np.arange(0,10,80)
amp=np.cos(time)
#generating cos wave
plot.ylabel("AMPLITUDE")
plot.subplot(1,2,1)
plot.plot(time,amp)
print("\nthe time values:-",time)
print("\nthe amp values:-",amp)
plot.title("GENERATING COS WAVE")
plot.xlabel("TIME")
#generating sine wave
print("\nthe time values:-",time)
print("\nthe amp values:-",amp)
time1=np.linspace(0,10,80)
amp1=np.sin(time)
plot.subplot(1,2,2)
plot.plot(time1,amp1)
plot.title("GENERATING SIN WAVE")
plot.xlabel("TIME")
plot.ylabel("AMPLITUDE")
plot.show()



