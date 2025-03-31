import time
import csv
import os
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import Adafruit_DHT
import RPi.GPIO as GPIO

# Konfiguration
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = [25, 7, 5, 6, 8]  # GPIO-Pins für die DHT22-Sensoren
MIC_PIN = [24, 17, 22, 23, 27]  # GPIO-Pins für die Mikrofone (Transistorsteuerung)
NUM_BEEHIVES = len(DHT_PIN)
RECORD_SECONDS = 5  # Dauer der Tonaufnahme in Sekunden
SAMPLE_RATE = 48000  # Abtastrate für die Audioaufnahme
CSV_FILE = 'beehive_data.csv'

# GPIO initialisieren
GPIO.setmode(GPIO.BCM)
for pin in MIC_PIN:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  # Mikrofone standardmäßig deaktivieren


# Funktion zum Aufnehmen von Audio
def record_audio(beehive_id):
    print(f"Aufnahme von Bienenstock {beehive_id + 1}...")
    audio_data = sd.rec(int(RECORD_SECONDS * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, device=1)
    sd.wait()  # Warten, bis die Aufnahme abgeschlossen ist
    print(f"Aufnahme von Bienenstock {beehive_id + 1} abgeschlossen.")
    return audio_data


# Funktion zum Speichern der Audioaufnahme
def save_audio(audio_data, beehive_id):
    filename = f"beehive_{beehive_id + 1}_audio.wav"
    write(filename, SAMPLE_RATE, audio_data)
    print(f"Audio für Bienenstock {beehive_id + 1} gespeichert als {filename}.")


# Funktion zum Auslesen von Temperatur und Luftfeuchtigkeit
def read_dht_sensor(beehive_id):
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN[beehive_id])
    return temperature, humidity


# CSV-Datei initialisieren
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Datum', 'Bienenstock', 'Temperatur (°C)', 'Luftfeuchtigkeit (%)'])

# Hauptschleife
try:
    GPIO.cleanup()
    while True:
        for beehive_id in range(NUM_BEEHIVES):
            # Mikrofon aktivieren
            GPIO.output(MIC_PIN[beehive_id], GPIO.HIGH)
            time.sleep(0.1)  # Kurze Wartezeit, um sicherzustellen, dass das Mikrofon bereit ist

            # Temperatur und Luftfeuchtigkeit auslesen
            temperature, humidity = read_dht_sensor(beehive_id)
            if temperature is not None and humidity is not None:
                # Aktuelles Datum und Uhrzeit
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")

                # Audio aufnehmen
                audio_data = record_audio(beehive_id)

                # Audio speichern
                save_audio(audio_data, beehive_id)

                # Daten in CSV speichern
                with open(CSV_FILE, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([current_time, beehive_id + 1, temperature, humidity])

                print(f"Daten für Bienenstock {beehive_id + 1} gespeichert.")
            else:
                print(f"Fehler beim Auslesen des Sensors für Bienenstock {beehive_id + 1}.")

            # Mikrofon deaktivieren
            GPIO.output(MIC_PIN[beehive_id], GPIO.LOW)

            # Kurze Pause zwischen den Bienenstöcken
            time.sleep(1)

except KeyboardInterrupt:
    print("Programm beendet.")
finally:
    GPIO.cleanup()  # GPIO-Pins zurücksetzen