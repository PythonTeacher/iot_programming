import picamera
import time

camera = picamera.PiCamera()

camera.start_preview()
time.sleep(5)
camera.stop_preview()
