import RPi.GPIO as GPIO

LDR_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LDR_PIN, GPIO.IN)

try:
    while True:
        # 0(어두움) 또는 1(밝음)로 출력
        read = GPIO.input(LDR_PIN)
        print(read)
finally:
    print('cleanup and exit')
    GPIO.cleanup()
