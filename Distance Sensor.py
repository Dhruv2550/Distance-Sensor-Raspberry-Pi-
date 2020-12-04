from gpiozero import DistanceSensor
from time import sleep
from datetime import datetime

ds = DistanceSensor()

while True:
    time_before = (datetime.now())
    sleep(0.5)
    distance = 50
    time_after = (datetime.now())
    speed = distance/time_before



    time = (time_after-time_before)
    microsecond = int(time.microseconds)

    second = microsecond / 1000000
    print(second)

    print(speed)
