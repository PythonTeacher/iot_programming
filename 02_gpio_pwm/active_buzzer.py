import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

GPIO.output(BUZZER_PIN, GPIO.HIGH)
time.sleep(2)
GPIO.output(BUZZER_PIN, GPIO.LOW)

GPIO.cleanup()
