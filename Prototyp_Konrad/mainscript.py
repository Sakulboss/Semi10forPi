import RPi.GPIO as GPIO
import time
import os
from record import record
from temp import read_and_save_dht_sensors

# Konfiguration
GPIO_PINS = {
    'audio_pin_1': 22,
    'audio_pin_2': 17,
    'audio_pin_3': 27,
}
DHT_PINS = [7, 5, 6, 8]  # GPIO-Pins für die DHT-Sensoren
RECORD_DURATION = 60  # Dauer der Aufnahme in Sekunden
SLEEP_DURATION = 1  # Pause zwischen den Aufnahmen

# GPIO initialisieren
def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    for pin in GPIO_PINS.values():
        GPIO.setup(pin, GPIO.OUT)

# GPIO freigeben
def cleanup_gpio():
    GPIO.cleanup()

# Hauptfunktion
def main():
    setup_gpio()
    try:
        i = 0
        while True:
            for pin in [GPIO_PINS['audio_pin_1'], GPIO_PINS['audio_pin_2']]:
                record(RECORD_DURATION, pin, True)  # Aufnahme für 60 Sekunden
                read_and_save_dht_sensors(DHT_PINS)
                print("Temperaturdaten gespeichert.")
                time.sleep(SLEEP_DURATION)
                i += 1
                print(f"Aufnahme-Zyklus: {i}")

            # Optional: Neustart nach einer bestimmten Anzahl von Zyklen
            if i >= 1000:
                print("Neustart des Systems...")
                os.system("sudo shutdown -r now")
                break  # Beende die Schleife nach dem Neustart

    except KeyboardInterrupt:
        print("Programm wurde durch den Benutzer beendet.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    finally:
        cleanup_gpio()

if __name__ == "__main__":
    main()