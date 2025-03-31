import adafruit_dht
import board
import datetime
import RPi.GPIO as GPIO
import time

def test_transistor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(14, GPIO.OUT)

    GPIO.output(17, GPIO.LOW)
    time.sleep(10)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(10)


def read_temp(pin):
    temps =[]
    dht_device = adafruit_dht.DHT22(board.D4)

    temp = dht_device.temperature
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temps.append((time, temp, pin))
    return temps