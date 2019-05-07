#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

#PWM com 100Hz de frequencia
left_forward = GPIO.PWM(16, 100)
right_forward = GPIO.PWM(15, 100)
left_back = GPIO.PWM(13, 100)
right_back = GPIO.PWM(11, 100)

left_forward.start(0)
right_forward.start(0)
left_back.start(0)
right_back.start(0)

print 'testing'

while 1:
        print 'working'
        left_forward.ChangeDutyCycle(20)
        right_forward.ChangeDutyCycle(20)
        time.sleep(2)
        left_forward.ChangeDutyCycle(0)
        right_forward.ChangeDutyCycle(0)

        left_back.ChangeDutyCycle(20)
        right_back.ChangeDutyCycle(20)
        time.sleep(2)
        left_back.ChangeDutyCycle(0)
        right_back.ChangeDutyCycle(0)


GPIO.cleanup()



