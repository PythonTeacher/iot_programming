import RPi.GPIO as GPIO

LED_PIN = 3
BUTTON_PIN = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

led_on = False
old_val = 0

try:
    while True:
        val = GPIO.input(BUTTON_PIN)

        if old_val == 0 and val == 1:
            print('Rising Edge')
            led_on = not led_on
            GPIO.output(LED_PIN, led_on)
        elif old_val == 1 and val == 0:
            print('Falling Edge')

        old_val = val
finally:
    GPIO.cleanup()
