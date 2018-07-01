import machine, neopixel
import time

np = neopixel.NeoPixel(machine.Pin(25), 12)

def clear(np):
    n = np.n
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()


def cycle(np, number, wait = 25, color = 'white'):
    n = np.n
    #clear(np)

    if (number // 256) % 2 == 0:
        brightness = number & 0xff
    else:
        brightness = 255 - (number & 0xff)

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

    np[number % n] = c
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

    # cycle
    for i in range(4 * n):
        cycle(np, i, 150, color='white')

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

try:
    while True:
        demo(np)
except KeyboardInterrupt:
    print("quit the demo")
finally:
    clear(np)
