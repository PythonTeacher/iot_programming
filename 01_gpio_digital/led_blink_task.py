import RPi.GPIO as GPIO  # GPIO 모듈 import
import time

R_LED_PIN = 4             # PIN 번호 설정
Y_LED_PIN = 5
G_LED_PIN = 6
GPIO.setmode(GPIO.BCM)  # 핀 번호 방식 설정 (GPIO.BOARD or GPIO.BCM)
GPIO.setup(R_LED_PIN, GPIO.OUT)  # PIN 모드 설정 (GPIO.OUT or GPIO.IN)
GPIO.setup(Y_LED_PIN, GPIO.OUT)  # PIN 모드 설정 (GPIO.OUT or GPIO.IN)
GPIO.setup(G_LED_PIN, GPIO.OUT)  # PIN 모드 설정 (GPIO.OUT or GPIO.IN)

GPIO.output(R_LED_PIN, GPIO.HIGH)  # True, 1
print("Red Led on")
time.sleep(2)
GPIO.output(R_LED_PIN, GPIO.LOW)

GPIO.output(Y_LED_PIN, GPIO.HIGH)  # False, 0
print("Yellow Led on")
time.sleep(2)
GPIO.output(Y_LED_PIN, GPIO.LOW)

GPIO.output(G_LED_PIN, GPIO.HIGH)  # False, 0
print("Green Led on")
time.sleep(2)
GPIO.output(G_LED_PIN, GPIO.LOW)

GPIO.cleanup()          # GPIO 핀상태 초기화
