import RPi.GPIO as GPIO
import time

TRIG_PIN = 4
ECHO_PIN = 14
LED_PIN = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)  # 10us (microsec)
        GPIO.output(TRIG_PIN, False)

        while GPIO.input(ECHO_PIN) == 0:    # 펄스 발생 중
            pass
        start = time.time()     # ECHO PIN HIGH (시작)

        while GPIO.input(ECHO_PIN) == 1:    # 펄스 발생 종료
            pass
        stop = time.time()      # ECHO PIN LOW (종료)

        duration_time = stop - start
        distance = duration_time * 17160  # 34321/2

        print('Distance: %.1fcm' % distance)

        if distance <= 20:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print('LED on')
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            print('LED off')

        time.sleep(0.1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')
