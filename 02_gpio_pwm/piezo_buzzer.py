import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 262)  # 4옥타브 도음 (262 주파수)
pwm.start(50)

time.sleep(2)
pwm.ChangeDutyCycle(0)  # 부저음이 나지 않음

pwm.stop()
GPIO.cleanup()
