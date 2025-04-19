from record import *
from temp import *

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

gpio_pins = [7, 5, 6, 8]  # 25 ist Stock 1 GPIO-Pins für die DHT-Sensoren
i=0

while True:
    record(60, 22, True)  # Aufnahme fuer 60 Sekunden und speichere die Datei
    read_and_save_dht_sensors(gpio_pins)
    print("Temperaturdaten gespeichert.")
    sleep(1)
    record(60, 17, True)  # Aufnahme fuer 60 Sekunden und speichere die Datei
    read_and_save_dht_sensors(gpio_pins)
    print("Temperaturdaten gespeichert.")
    sleep(1)
    i=i+1
    print(i)
    if i==3:
        print("Neustart des Systems...")
        os.system("sudo shutdown -r now")