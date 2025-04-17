from record import *
from temp import *

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

gpio_pins = [25, 7, 5, 6, 8]  # GPIO-Pins für die DHT-Sensoren

while True:
    record(60, 22)  # Aufnahme fuer 60 Sekunden und speichere die Datei
    read_and_save_dht_sensors(gpio_pins)
    print("Temperaturdaten gespeichert.")
    sleep(1)
    record(60, 17)  # Aufnahme fuer 60 Sekunden und speichere die Datei
    read_and_save_dht_sensors(gpio_pins)
    print("Temperaturdaten gespeichert.")
    sleep(1)