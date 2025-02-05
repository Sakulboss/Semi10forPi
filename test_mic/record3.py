import sounddevice as sd
from scipy.io.wavfile import write

fs = 48000  # Sample rate
seconds = 60  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('../output2.wav', fs, myrecording)  # Save as WAV file
