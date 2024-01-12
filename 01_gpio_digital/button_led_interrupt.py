# Git Test

import RPi.GPIO as GPIO
import time

LED_PIN = 3
BUTTON_PIN = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

led_on = False


def button_callback(channel):
    global led_on
    led_on = not led_on
    print("LED : ", led_on)
    GPIO.output(LED_PIN, led_on)


# 시간차이로 오차가 생길 수 있음
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING,
                      callback=button_callback, bouncetime=100)

#GPIO.add_event_detect(18, GPIO.RISING, callback=rising, bouncetime=100)
#GPIO.add_event_detect(18, GPIO.FALLING, callback=falling, bouncetime=100)

while True:
    time.sleep(100)
