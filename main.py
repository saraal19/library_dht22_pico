from machine import I2C, Pin
from dht22 import DHT22
from time import sleep
import time

dht22=DHT22(Pin(15,Pin.IN,Pin.PULL_UP))

while True:
    T, H = dht22.read()
    print(str(T)+"C")
    print(str(H))
    time.sleep_ms(500)
