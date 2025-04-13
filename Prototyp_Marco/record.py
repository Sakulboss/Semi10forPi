import sounddevice as sd
from scipy.io.wavfile import write
from time import *
from datetime import datetime
import os
import RPi.GPIO as GPIO

def get_new_filename(file_extension: str) -> str:

    count = len([i for i in os.listdir() if i.endswith(file_extension)])

    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')  # Formatierung ohne Doppelpunkte

    return f'output_{timestamp}_{count}.{file_extension}'

def pathway():
	pass

def aufnahmen(seconds: float, fs = 48000, printRecording = False) -> None:
	myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, device=1)
	print('Aufnahme gestartet.')
	sleep(seconds + 1)
	#sd.wait()  # Wait until recording is finished
	print('Aufnahme fertig')
	if printRecording:
		print(myrecording)
	return myrecording

def speichern(myrecording, fs =  48000) -> None:
	write(get_new_filename("wav"), fs, myrecording)  # Save as WAV file
	print('Programmende')

def main(dauer):
	print(sd.query_devices())
	speichern(aufnahmen(dauer))

if __name__ == '__main__':
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(17, GPIO.OUT)
	GPIO.setup(27, GPIO.OUT)
	GPIO.setup(22, GPIO.OUT)
	GPIO.output(17, GPIO.LOW)
	GPIO.output(27, GPIO.LOW)
	GPIO.output(22, GPIO.LOW)
	sleep(1)
	main(10)
	# fs: Sample rate
	# seconds: Duration of recording
