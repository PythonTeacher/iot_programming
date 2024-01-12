import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

melody = [0, 262, 294, 330, 349, 392, 440, 494, 523]
#      솔 솔 라 라 솔 솔 미  솔 솔 미 미 레
#      솔 솔 라 라 솔 솔 미  솔 미 레 미 도
idx = [5, 5, 6, 6, 5, 5, 3,  5, 5, 3, 3, 2,
       5, 5, 6, 6, 5, 5, 3,  5, 3, 2, 3, 1]

try:
    for i in range(0, len(idx)):
        pwm.ChangeFrequency(melody[idx[i]])
        if i == 6 or i == 18:
            time.sleep(1)
        elif i == 11 or i == 23:
            time.sleep(2)
        else:
            time.sleep(0.5)

finally:
    pwm.stop()
    GPIO.cleanup()
