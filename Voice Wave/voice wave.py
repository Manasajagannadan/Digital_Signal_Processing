#testing the voice
import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('sai.wav')
print(fs,len(data),data)
plt.subplot(211)
plt.plot(data)
t=np.arange(0,len(data)/fs,1.0/fs)
plt.subplot(212)
plt.plot(t,data)
plt.show()
wav.write('manu-slow.wav',0.5*fs,data)
#wav.write('manu-fast.wav',0.5*fs,data)
#data1=np.array(data1,dtype='uint8')
#t1=np.arrange(0,len(data)/np.float(fs),1.0/fs)
#print(fs,len(data),t1)ss

