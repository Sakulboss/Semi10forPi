import sounddevice as sd
from scipy.io.wavfile import write
from time import *
import RPi.GPIO as GPIO
from pydub import AudioSegment
import os
from datetime import datetime

#Flac

def cflac(wav_file_path):
    # Load the WAV file
    audio = AudioSegment.from_wav(wav_file_path)

    # Create the output file path by changing the extension to .flac
    flac_file_path = os.path.splitext(wav_file_path)[0] + '.flac'

    # Export as FLAC
    audio.export(flac_file_path, format="flac")
    print(f"Converted {wav_file_path} to {flac_file_path}")


def cwav(flac_file_path):
    # Load the FLAC file
    audio = AudioSegment.from_file(flac_file_path, format="flac")
    # Create the output file path by changing the extension to .wav
    wav_file_path = os.path.splitext(flac_file_path)[0] + '.wav'
    # Export as WAV
    audio.export(wav_file_path, format="wav")
    print(f"Converted {flac_file_path} to {wav_file_path}")

# Splitting

def split_stereo_to_mono(wav_file_path):
	# Load the stereo WAV file
	audio = AudioSegment.from_wav(wav_file_path)
	# Check if the audio is stereo
	if audio.channels != 2:
		raise ValueError("The input file is not a stereo WAV file.")
	# Split into left and right channels
	left_channel = audio.split_to_mono()[0]
	right_channel = audio.split_to_mono()[1]
	# Create output file paths
	base_name = os.path.splitext(wav_file_path)[0]
	left_channel_path = f"{base_name}_left.wav"
	right_channel_path = f"{base_name}_right.wav"
	# Export the mono channels as separate WAV files
	left_channel.export(left_channel_path, format="wav")
	right_channel.export(right_channel_path, format="wav")
	print(f"Split {wav_file_path} into {left_channel_path} and {right_channel_path}")

#Filename generator

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

#aufnehmen

def aufnahmen(seconds: float, gpio, fs = 48000, printRecording = False) -> None:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(gpio, GPIO.OUT)
	GPIO.output(gpio, GPIO.HIGH)
	myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, device=1)
	print('Aufnahme gestartet.')
	sleep(seconds + 1)
	#sd.wait()  # Wait until recording is finished
	print('Aufnahme fertig')
	if printRecording:
		print(myrecording)
	GPIO.output(gpio, GPIO.LOW)
	return myrecording

def speichern(myrecording, gpio, fs =  48000) -> None:
	write(get_new_filename("wav",gpio), fs, myrecording)  # Save as WAV file
	#print('Programmende')

def record(dauer, gpio):
	#print(sd.query_devices())
	speichern(aufnahmen(dauer),gpio)

if __name__ == '__main__':
	record(10,22)

