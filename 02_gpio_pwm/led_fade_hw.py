# pip3 install wiringpi
# sudo python3 led_fade_hw.py (pwm관련 레지스터에 접근해야 하므로 sudo를 붙여야 함)
import wiringpi as wpi
PIN_LED = 12

wpi.wiringPiSetupGpio()
wpi.pinMode(PIN_LED, wpi.PWM_OUTPUT)

while True:
    for i in range(0, 1024):
        wpi.pwmWrite(PIN_LED, i)
        wpi.delay(1)
    for i in range(1024, -1, -1):
        wpi.pwmWrite(PIN_LED, i)
        wpi.delay(1)
