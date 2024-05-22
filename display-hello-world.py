import threading
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
import time

def display_text():
    serial = i2c(port=1, address=0x3C)
    device = ssd1306(serial)
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((30, 40), "Hello World", fill="white")

# Create a thread for the display_text function
t = threading.Thread(target=display_text)

# Start the thread
t.start()

# Let it run for 60 seconds
time.sleep(60)

# If the thread is still running after 60 seconds, stop it
if t.is_alive():
    print("Stopping thread")
    t._stop()
