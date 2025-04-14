import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.output(17, GPIO.HIGH) # S0
GPIO.output(27, GPIO.LOW) # S1
GPIO.output(22, GPIO.LOW) # S2

#time.sleep(10)