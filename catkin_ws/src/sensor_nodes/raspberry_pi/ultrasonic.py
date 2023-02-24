#!/usr/bin/python3
# import RPi.GPIO as GPIO
import time
from ultrasonic_node import *

### ultrasonic pins ###
trigPin1 = 18
echoPin1 = 24
index1 = 1

if __name__ == "__main__":
        us1 = ultrasonic(trigPin1, echoPin1, index1)
        while True:
            us1.ultrasonic_pub.publish(1)
