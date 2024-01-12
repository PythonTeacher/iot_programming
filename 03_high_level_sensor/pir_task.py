import RPi.GPIO as GPIO
import time

PRI_PIN = 4
LED_PIN = 14
BUZZER_PIN = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(PRI_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)   # 처음에는 소리나지 않음
pwm.start(50)

time.sleep(5)
print('PIR Ready...')

try:
    while True:
        val = GPIO.input(PRI_PIN)
        if val == GPIO.HIGH:
            print('움직임 감지')
            GPIO.output(LED_PIN, GPIO.HIGH)
            pwm.ChangeFrequency(392)    # 솔음
        else:
            print('움직임 없음')
            GPIO.output(LED_PIN, GPIO.LOW)
            pwm.ChangeFrequency(1)  # 부저음이 나지않게 함

        time.sleep(0.1)

finally:
    GPIO.cleanup()
    pwm.stop()
    print('cleanup and exit')
