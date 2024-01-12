import RPi.GPIO as GPIO

LDR_PIN = 18

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LDR_PIN, GPIO.IN)

    val = -1

    while True:
        read = GPIO.input(LDR_PIN)
        if read != val:
            val = read
            print(val)

finally:
    print("clean up")
    GPIO.cleanup()
