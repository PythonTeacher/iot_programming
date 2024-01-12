import RPi.GPIO as GPIO
import time

TRIG_PIN = 4
ECHO_PIN = 14
BUZZER_PIN = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)  # 처음에는 소리나지 않음
pwm.start(50)
time.sleep(2)

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

        if distance <= 10:
            print('buzzer on 1')
            pwm.ChangeFrequency(392)    # 솔음
            time.sleep(0.5)
        elif distance <= 30:
            print('buzzer on 2')
            pwm.ChangeFrequency(392)    # 솔음
            time.sleep(1)

        pwm.ChangeFrequency(1)  # 부저음이 나지않게 함
        time.sleep(0.1)
finally:
    GPIO.cleanup()
    pwm.stop()
    print('cleanup and exit')
