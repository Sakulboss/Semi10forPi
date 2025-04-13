import sounddevice as sd
from scipy.io.wavfile import write
from time import *
from datetime import datetime
import os
import RPi.GPIO as GPIO

import os

from datetime import datetime


def get_new_filename(file_extension: str, number: int) -> str:
	# Erstelle den Ordner "Aufnahmen", falls er nicht existiert
	folder_name = 'Aufnahmen'
	if not os.path.exists(folder_name):
		os.makedirs(folder_name)
	count = len([i for i in os.listdir(folder_name) if i.endswith(file_extension)])
	timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')  # Formatierung ohne Doppelpunkte
	filename = f'output_{timestamp}_{count}_{number}.{file_extension}'
	# Vollständiger Pfad zur Datei
	full_path = os.path.join(folder_name, filename)
	return full_path

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

def speichern(myrecording, fs =  48000, number) -> None:
	write(get_new_filename("wav",number), fs, myrecording)  # Save as WAV file
	#print('Programmende')

def main(dauer, number):
	#print(sd.query_devices())
	speichern(aufnahmen(dauer),number)

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
