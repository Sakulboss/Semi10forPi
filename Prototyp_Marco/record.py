import sounddevice as sd
from scipy.io.wavfile import write as writewav
from time import *
import os
import RPi.GPIO as GPIO
from pydub import AudioSegment
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

def speichern(myrecording, number, flac, fs =  48000) -> None:
	if flac:
		# Save as WAV file
		filepath = get_new_filename("wav", number)
		writewav(filepath, fs, myrecording)

		# Convert to FLAC
		flac_file_path = os.path.splitext(filepath)[0] + '.flac'
		audio = AudioSegment.from_wav(filepath)
		audio.export(flac_file_path, format="flac")
		os.remove(filepath)
	else:
		writewav(get_new_filename("wav", number), fs, myrecording)  # Save as WAV file

def record(dauer, number, flac):
	#print(sd.query_devices())
	speichern(aufnahmen(dauer), number, flac)

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
