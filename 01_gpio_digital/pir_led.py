import RPi.GPIO as GPIO
import time

LED_PIN = 8
PIR_PIN = 7

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)
#GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    while True:
        val = GPIO.input(PIR_PIN)
        print(val)
        GPIO.output(LED_PIN, val)
        time.sleep(0.1)
finally:
    GPIO.cleanup()
