import RPi.GPIO as GPIO
import time

BUTTON_PIN = 8

GPIO.setmode(GPIO.BCM)
#GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        val = GPIO.input(BUTTON_PIN)
        print(val)
        time.sleep(0.1)
finally:
    GPIO.cleanup()
