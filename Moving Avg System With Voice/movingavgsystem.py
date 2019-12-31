#to generate a .mp3/wav with our voice,but here iam talking other cloud google voice and myfrnd's voice.wav and apply noise for that signal and apply moving average system again here our original signal
print("\nMOVING AVERAGE SYSTEM")
print("\nBY: MANASA J")
input('\nPress "manu" to Start:-')
import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
def mean(lst): return sum(lst)/len(lst)
#applying our voice::-
fs,data=wav.read('voice.wav')
t=np.arange(0,len(data)/fs,1.0/fs)
plt.subplot(311)
plt.title("WAV")
plt.xlabel("TIME")
plt.ylabel("AMPLITUDE")
plt.plot(t,data)
plt.subplot(312)
#applying noise for the .wav system::-
noise = np.random.normal(0,10,data.shape)
#noise2=int(noise)
# 0 is the mean of the normal distribution you are choosing from
# 1 is the standard deviation of the normal distribution
# 100 is the number of elements you get in array noise
a = list([data])
noise1=data + noise
plt.title("NOISE")
plt.xlabel("TIME")
plt.ylabel("AMPLITUDE")
plt.plot(noise1)
plt.subplot(313)
data=abs(data)
#applying moving average system::-
env=np.zeros_like(data)
#env2.np.zeros_like(data)
for i in range(len(data)):
    env[i]=mean(data[max(i-1000,0):i+1])
plt.plot(range(len(data)), env, color='red')
plt.title("MEAN AVERAGE SYSTEM")
plt.xlabel("TIME")
plt.ylabel("AMPLITUDE")
plt.show()

