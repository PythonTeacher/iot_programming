from lcd import drivers
import time
import datetime
import Adafruit_DHT

display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
PIN = 18

try:
    while True:
        now = datetime.datetime.now()
        display.lcd_display_string(now.strftime("%x%X"), 1)
        h, t = Adafruit_DHT.read_retry(sensor, PIN)
        if h is not None and t is not None:
            display.lcd_display_string('%.1f*C, %.1f%%' % (t, h), 2)
        else:
            display.lcd_display_string('Read error', 2)
        time.sleep(2)
finally:
    print("Cleaning up!")
    display.lcd_clear()
