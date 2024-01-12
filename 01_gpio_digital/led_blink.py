import RPi.GPIO as GPIO  # GPIO 모듈 import
import time

PIN_LED = 4             # PIN 번호 설정
GPIO.setmode(GPIO.BCM)  # 핀 번호 방식 설정 (GPIO.BOARD or GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)  # PIN 모드 설정 (GPIO.OUT or GPIO.IN)

for i in range(5):
    GPIO.output(PIN_LED, GPIO.HIGH)  # True, 1
    print("Led on")
    time.sleep(1)
    GPIO.output(PIN_LED, GPIO.LOW)  # False, 0
    print("Led off")
    time.sleep(1)

GPIO.cleanup()          # GPIO 핀상태 초기화
