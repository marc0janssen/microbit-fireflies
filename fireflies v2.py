# Name: Fireflies
# Coder: Marco Janssen (twitter @marc0janssen)
# date: 2021-03-30
# version: 1.0.0


from microbit import display, sleep
import random

# This fucntions fixes the "display.get_pixel" bug.
# a full bright led does not return a "9" but a "255".


def fixPixelBug(brightness):
    if brightness == 4:
        return 3
    elif brightness == 8:
        return 4
    elif brightness == 16:
        return 5
    elif brightness == 32:
        return 6
    elif brightness == 64:
        return 7
    elif brightness == 128:
        return 8
    elif brightness == 255:
        return 9
    else:
        return brightness


while True:
    sleep(50)

    brightness = random.randint(1, 9)
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    if display.get_pixel(x, y) == 0:
        display.set_pixel(x, y, brightness)

    for fireflies in range(0, 5):
        x = random.randint(0, 4)
        y = random.randint(0, 4)

        if fixPixelBug(display.get_pixel(x, y)) > 0:
            display.set_pixel(x, y, fixPixelBug(display.get_pixel(x, y)) - 1)
