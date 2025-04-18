from record import *
from temp import *

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

while True:
    #reading hive 1 and 2
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    main(60,1, True)
    save_temp(read_temp())
    sleep(1)
    # 3 and 4
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    main(60,2,True)
    save_temp(read_temp())
    sleep(1)