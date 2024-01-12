import RPi.GPIO as GPIO
import time

PIN_LED = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)

pwm = GPIO.PWM(PIN_LED, 100)
pwm.start(0)  # duty_cycle (0~100)

try:
    while True:
        for i in range(0, 101):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.01)
        for i in range(100, -1, -1):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.01)
finally:
    pwm.stop()
    GPIO.cleanup()
