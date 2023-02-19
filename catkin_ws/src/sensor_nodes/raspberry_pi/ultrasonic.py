import RPi._GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trig = 16
echo = 18
print("Distance Measurement in progress")
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)
print("Waiting for sensor ro settle")
time.sleep(2)
GPIO.output(trig, False)
time.sleep(0.00001)
GPIO.output(trig, False)
while GPIO.input(echo) == 0:
    pulse_start = time.time()
while GPIO.input(echo) == 1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17150
distance = round(distance, 2)
print("Distance :", distance, "cm")