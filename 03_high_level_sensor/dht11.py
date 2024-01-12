import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
PIN = 4

try:
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, PIN)
        if h is not None and t is not None:
            print('Temperature=%.1f*, Humidity:%.1f%%' % (t, h))
        else:
            print('Read error')

finally:
    print('bye')
