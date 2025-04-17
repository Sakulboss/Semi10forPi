import sounddevice as sd
from scipy.io.wavfile import write as writewav
from time import *
import RPi.GPIO as GPIO
from pydub import AudioSegment
import os
from datetime import datetime
import io

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
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, device=0)
    print('Aufnahme gestartet.')
    sleep(seconds + 1)
    #sd.wait()  # Wait until recording is finished
    print('Aufnahme fertig')
    if printRecording:
        print(myrecording)
    GPIO.output(gpio, GPIO.LOW)
    return myrecording


def speichern(myrecording, gpio, flac, fs=48000) -> None:
    if flac:
        # Erstelle ein AudioSegment aus myrecording
        audio = AudioSegment(
            myrecording.tobytes(),
            frame_rate=fs,
            sample_width=myrecording.dtype.itemsize,
            channels=2  # die Anzahl der Kanäle, die myrecording hat
        )
        # Exportiere direkt als FLAC
        audio.export(get_new_filename("flac", gpio), format="flac")
    else:
        # Speichere als WAV-Datei
        writewav(get_new_filename("wav", gpio), fs, myrecording)

def record(dauer, gpio,flac):
    #print(sd.query_devices())
    speichern(aufnahmen(dauer,gpio),gpio,flac)

if __name__ == '__main__':
    record(10,22)

