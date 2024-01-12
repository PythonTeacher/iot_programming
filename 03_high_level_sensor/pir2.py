import RPi.GPIO as GPIO
import time

PRI_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PRI_PIN, GPIO.IN)
old_val = -1

try:
    while True:
        val = GPIO.input(PRI_PIN)
        if val != old_val:
            old_val = val
            if val == 0:
                print('움직임 없음')
            else:
                print('움직임 감지')

        time.sleep(0.5)

finally:
    GPIO.cleanup()
    print('cleanup and exit')
