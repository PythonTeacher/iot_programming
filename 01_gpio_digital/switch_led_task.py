import RPi.GPIO as GPIO

R_LED_PIN = 9
Y_LED_PIN = 10
G_LED_PIN = 11

R_SWITCH_PIN = 16
Y_SWITCH_PIN = 20
G_SWITCH_PIN = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(R_LED_PIN, GPIO.OUT)
GPIO.setup(Y_LED_PIN, GPIO.OUT)
GPIO.setup(G_LED_PIN, GPIO.OUT)
GPIO.setup(R_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Y_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(G_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        val = GPIO.input(R_SWITCH_PIN)
        print(val)
        GPIO.output(R_LED_PIN, val)

        val2 = GPIO.input(Y_SWITCH_PIN)
        print(val2)
        GPIO.output(Y_LED_PIN, val2)

        val3 = GPIO.input(G_SWITCH_PIN)
        print(val3)
        GPIO.output(G_LED_PIN, val3)
finally:
    GPIO.cleanup()
    print('cleanup and exit')
