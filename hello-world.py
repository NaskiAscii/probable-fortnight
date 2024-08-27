import ST7789
import time
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont

# Configuration for CS and DC pins:
CS_PIN = 8
DC_PIN = 25
RST_PIN = 27
LED_PIN = 24

# Create TFT LCD display class.
disp = ST7789.ST7789(
    port=0,
    cs=CS_PIN,
    dc=DC_PIN,
    backlight=LED_PIN,
    rst=RST_PIN,
    spi_speed_hz=80 * 1000 * 1000,
    width=240,
    height=320
)

# Initialize display.
disp.begin()

# Clear the display to a red background.
disp.clear(ST7789.RED)

# Create blank image for drawing.
image = Image.new('RGB', (240, 320), color=(0, 0, 0))
draw = ImageDraw.Draw(image)

# Load a TTF font.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

# Draw Some Text
text = "Hello, World!"
(font_width, font_height) = font.getsize(text)
draw.text(
    (disp.width // 2 - font_width // 2, disp.height // 2 - font_height // 2),
    text,
    font=font,
    fill=(255, 255, 0)
)

# Display image.
disp.display(image)

# Keep the script running.
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Turn off backlight on control-c
    disp.set_backlight(0)
