import machine, neopixel
from machine import Pin
import time
import random

# NeoPixel on Pin25, 12 LEDs
np = neopixel.NeoPixel(Pin(25), 12)

# Button on Pin14
button = Pin(14, Pin.IN, Pin.PULL_UP)
button_state = True


def callback(pin):
    # wait for pin to change value
    # it needs to be stable for a continuous 20ms
    global button_state
    cur_value = pin.value()
    active = 0
    while active < 50:
        if pin.value() != cur_value:
            active += 1
        else:
            active = 0
    if active > 0:
        if button_state == False:
            button_state = True
        else:
            button_state = False


def clear(np):
    n = np.n
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()


def disco(np, step=32):
    n = np.n
    for i in range(n):
        for j in range(n):
            np[j] = tuple((max(0, val - step) for val in np[j]))
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            np[i] = (r, g, b)
            np.write()
            time.sleep_ms(50)


def cycle(np, number, wait=25, color='white', brightness=None, debug=None):
    n = np.n
    led = number % n

    if not brightness:
        if (number // 256) % 2 == 0:
            brightness = number & 0xff
        else:
            brightness = 255 - (number & 0xff)
        if brightness == 0:
            brightness = 10

    if color == 'off':
        c = (0, 0, 0)
    if color == 'red':
        c = (brightness, 0, 0)
    if color == 'green':
        c = (0, brightness, 0)
    if color == 'blue':
        c = (0, 0, brightness)
    if color == 'white':
        c = (brightness, brightness, brightness)

    if debug:
        print("l", led, wait, color, brightness)

    np[led] = c
    np.write()
    time.sleep_ms(wait)


def bounce(np, number, wait = 120):
    n = np.n
    for j in range(n):
        np[j] = (0, 0, 64)
    if (number // n) % 2 == 0:
        np[number % n] = (0, 0, 0)
    else:
        np[n - 1 - (number % n)] = (0, 0, 0)
    np.write()
    time.sleep_ms(wait)


def demo(np):
    n = np.n
    list_com = list(range(n,-1,-2)) + list(range(1,n,2))
    list_com.remove(n)
    clear(np)

    disco(np)
    time.sleep_ms(100)
    disco(np, step=128)
    clear(np)

    for i in list_com:
        cycle(np, i, 250, color='white', brightness=1)
    time.sleep_ms(100)

    for i in list_com:
        cycle(np, i, 250, color='white')
    time.sleep_ms(100)

    # cycle
    for i in range(4 * n):
        cycle(np, i, 150, color='white')
        cycle(np, i, 0, color='off')

    # cycle reverse to zero
    for i in range((4 * n -1), -1, -1):
        cycle(np, i, 150, color='red')

    # cycle
    for i in range(4 * n):
        cycle(np, i, 150, color='green')

    # cycle
    for i in range((4 * n -1), -1, -1):
        cycle(np, i, 150, color='blue')

    # bounce
    for i in range(4 * n):
        bounce(np, i, wait = 120)

    # fade in/out
    """
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, val, 0)
        np.write()
    """
    clear(np)

button.irq(trigger=Pin.IRQ_FALLING, handler=callback)

try:
    while True:
        if button_state == True:
            demo(np)

except KeyboardInterrupt:
    print("quit the demo")

finally:
    clear(np)

