import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.OUT)

print ("fan on")
GPIO.output(17, GPIO.LOW)
#time.sleep(10)