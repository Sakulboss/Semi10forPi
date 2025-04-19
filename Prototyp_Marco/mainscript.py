import RPi.GPIO as GPIO
import time
from record import record
from temp import read_temp, save_temp

# GPIO-Pins für den Multiplexer definieren
S0 = 17  # Pin für S0
S1 = 27  # Pin für S1
S2 = 22  # Pin für S2

n = 1  # 1/2 der Anzahl der Mikrofone

# GPIO initialisieren
GPIO.setmode(GPIO.BCM)
GPIO.setup(S0, GPIO.OUT)
GPIO.setup(S1, GPIO.OUT)
GPIO.setup(S2, GPIO.OUT)

def select_channel(channel):
    # Die Pins entsprechend dem gewünschten Kanal setzen
    GPIO.output(S0, channel & 0b0001)  # LSB
    GPIO.output(S1, (channel >> 1) & 0b0001)
    GPIO.output(S2, (channel >> 2) & 0b0001)

try:
    for channel in range(8):  # Angenommen, der Multiplexer hat 8 Kanäle
        select_channel(channel)
        time.sleep(1)  # Warten, um den Kanal zu stabilisieren
        record(60, channel, True)
        save_temp(read_temp())
finally:
    GPIO.cleanup()  # GPIO-Pins zurücksetzen