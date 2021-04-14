# Name: Fireflies
# Coder: Marco Janssen (twitter @marc0janssen)
# date: 2021-03-30
# version: 1.0.5


from microbit import display, sleep
from random import randint

while True:
    sleep(50)

    brightness = randint(1, 9)
    x = randint(0, 4)
    y = randint(0, 4)
    if display.get_pixel(x, y) == 0:
        display.set_pixel(x, y, brightness)

    for fireflies in range(0, 5):
        x = randint(0, 4)
        y = randint(0, 4)

        if display.get_pixel(x, y) > 0:
            display.set_pixel(x, y, display.get_pixel(x, y) - 1)
