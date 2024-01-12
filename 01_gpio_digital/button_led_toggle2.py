import RPi.GPIO as GPIO
import time

LED_PIN = 3
BUTTON_PIN = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

flag = 0

try:
    while True:
        val = GPIO.input(BUTTON_PIN)

        if val == GPIO.HIGH:    # 푸시버튼이 눌렸을 때
            if flag == 0:
                flag = 1
        else:                   # 푸시버튼이 떼어졌을 때
            if flag == 1:
                val2 = GPIO.input(LED_PIN)
                if val2 == GPIO.HIGH:
                    GPIO.output(LED_PIN, GPIO.LOW)
                else:
                    GPIO.output(LED_PIN, GPIO.HIGH)
            flag = 0
        time.sleep(0.1)
finally:
    GPIO.cleanup()
