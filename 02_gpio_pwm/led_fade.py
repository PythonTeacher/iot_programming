import RPi.GPIO as GPIO
import time

PIN_LED = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)

pwm = GPIO.PWM(PIN_LED, 50)  # PWM 인스턴스 생성, 주파수 설정
pwm.start(0)  # duty_cycle (0~100)

try:
    while True:
        for i in range(0, 101, 5):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.1)
        for i in range(100, -1, -5):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.1)
finally:
    pwm.stop()    # PWM 종료
    GPIO.cleanup()
