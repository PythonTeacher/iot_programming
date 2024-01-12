import RPi.GPIO as GPIO

PIN_LED = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)

try:
    while True: 
        val = input("1:on, 0:off > ")
        if val == '0':
            GPIO.output(PIN_LED, GPIO.LOW)
            print('Off')
        elif val == '1':
            GPIO.output(PIN_LED, GPIO.HIGH)
            print('On')
        else:
            break
finally:
    GPIO.cleanup()
    print('clean up and exit.')