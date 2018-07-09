import machine, neopixel
from machine import Pin
import time

# NeoPixel on Pin25, 12 LEDs
np = neopixel.NeoPixel(Pin(25), 12)

# Button on Pin14
button = Pin(14, Pin.IN)
state = False

# todo: yes this button bounces, thats a problem
def callback(p):
    global state
    if state == False:
        state = True
    else:
        state = False
    print('pin change', p, state)


def clear(np):
    n = np.n
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()


def cycle(np,number,wait=25,color='white',brightness=None,debug=None):
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
    """
    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()
    """

button.irq(trigger=Pin.IRQ_FALLING,handler=callback)
clear(np)

try:
    while True:
        if state == True:
            demo(np)
        else:
            clear(np)
except KeyboardInterrupt:
    print("quit the demo")
finally:
    clear(np)
