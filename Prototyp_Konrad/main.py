from record import *
from temp import *
from pydub import AudioSegment
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

def convert_all_wav_to_flac(folder_path):
    # Durchsuche den angegebenen Ordner nach WAV-Dateien
    for filename in os.listdir(folder_path):
        if filename.endswith(".wav"):
            wav_file_path = os.path.join(folder_path, filename)
            flac_file_path = os.path.splitext(wav_file_path)[0] + '.flac'

            # Lade die WAV-Datei und exportiere sie als FLAC
            audio = AudioSegment.from_wav(wav_file_path)
            audio.export(flac_file_path, format="flac")
            print(f"Umgewandelt: {wav_file_path} zu {flac_file_path}")

# Beispielaufruf
folder = "Aufnahmen"  # Ersetze dies durch den Pfad zu deinem Ordner
convert_all_wav_to_flac(folder)

gpio_pins = [25, 7, 5, 6, 8]  # GPIO-Pins für die DHT-Sensoren

while True:
    record(60, 22)  # Aufnahme für 60 Sekunden und speichere die Datei
    read_and_save_dht_sensors(gpio_pins)
    sleep(1)
    record(60, 17)  # Aufnahme für 60 Sekunden und speichere die Datei
    read_and_save_dht_sensors(gpio_pins)
    sleep(1)
    convert_all_wav_to_flac("Aufnahmen")