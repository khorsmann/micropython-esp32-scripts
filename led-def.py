# Connect IO25 to DIN
import machine, neopixel, time

def ringon(np):
    for i in range(65):
        np[(i + 11) % 12] = (0,0,0)
        np[i % 12] = ((i * 4) % 64, (i * 8) % 64, (i * 16) % 64)
        np.write()
        time.sleep_ms(40)

np = neopixel.NeoPixel(machine.Pin(25), 12)

