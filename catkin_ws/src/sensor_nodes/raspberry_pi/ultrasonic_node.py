#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import rospy
from std_msgs.msg import Int16

GPIO.setmode(GPIO.BOARD)

class ultrasonic():

    def __init__(self, trig, echo, index):
        self.trigPin = trig
        self.echoPin = echo
        self.index = index

        self.distance = Int16()
        self.publish_rate = 10

        GPIO.setup(self.trigPin, GPIO.OUT)
        GPIO.setup(self.echoPin, GPIO.IN)

        ### Publisher ###
        topic = "ultrasonic_"+str(self.index)+"_dis"
        self.ultrasonic_pub = rospy.Publisher(topic, Int16, queue_size=10)
        rospy.init_node("ultrasonic_"+str(self.index))
        self.rate = rospy.Rate(self.publish_rate)

        GPIO.output(self.trigPin, GPIO.LOW)
        print("Waiting for sensor to settle")

        self.distance_calculate()
    
    def distance_calculate(self):
        # while not rospy.is_shutdown():
        #     try:

        GPIO.output(self.trigPin, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(self.trigPin, GPIO.LOW)

        while GPIO.input(self.echoPin)==0:
            pulse_start_time = time.time()
        while GPIO.input(self.echoPin)==1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        self.distance.data = round(pulse_duration * 17150, 2)
        print("Distance:",self.distance.data,"cm")
    
    ### publish the distance ###
        self.ultrasonic_pub.publish(self.distance)
            
            # except rospy.ROSInterruptException :
            #     pass
            # self.rate.sleep()

if __name__ == "__main__":
    us = ultrasonic(18, 24, 1)
    
    while not rospy.is_shutdown():
        us.distance_calculate()
        us.rate.sleep()