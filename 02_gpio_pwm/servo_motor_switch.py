import RPi.GPIO as GPIO
import time

SWITCH_PIN = 4
SERVO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz, 1Period = 20ms
pwm.start(7.5)  # 7.5(0도)

count = 0
try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        if val == 0:
            print('count:', count)
            if count % 4 == 0:
                pwm.ChangeDutyCycle(7.5)
            elif count % 4 == 1:
                pwm.ChangeDutyCycle(2.5)
            elif count % 4 == 2:
                pwm.ChangeDutyCycle(7.5)
            else:
                pwm.ChangeDutyCycle(12.5)
            count += 1
            time.sleep(1)
finally:
    print("clean up and exit")
    pwm.stop()
    GPIO.cleanup()
