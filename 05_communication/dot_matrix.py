# import matrix module
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

import time

# create matrix device
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1, block_orientation=0,
                 rotate=0, blocks_arranged_in_reverse_order=False)
print("Created device")

# start demo
#msg = "MAX7219 LED Matrix Demo"
# print(msg)
#show_message(device, msg, fill="white", font=proportional(CP437_FONT))
# time.sleep(1)

# slow
msg = "Korea Digital Media High School"
print(msg)
show_message(device, msg, fill="white",
             font=proportional(LCD_FONT), scroll_delay=0.1)
