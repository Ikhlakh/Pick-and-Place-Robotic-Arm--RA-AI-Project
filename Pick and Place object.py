# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pins 11 & 12 as outputs, and define as PWM servo1 & servo2
GPIO.setup(16,GPIO.OUT)
servo1 = GPIO.PWM(16,50) # pin 11 for servo1
GPIO.setup(11,GPIO.OUT)
servo2 = GPIO.PWM(11,50) # pin 12 for servo2
GPIO.setup(13,GPIO.OUT)
servo3 = GPIO.PWM(13,50) # pin 11 for servo1
GPIO.setup(15,GPIO.OUT)
servo4 = GPIO.PWM(15,50) # pin 12 for servo2

while True:

    # Start PWM running on both servos, value of 0 (pulse off)
    servo1.start(0)
    servo2.start(0)
    servo3.start(0)
    servo4.start(0)

# Take Position
    servo2.ChangeDutyCycle(2)
    time.sleep(1)
    servo3.ChangeDutyCycle(12.5)
    time.sleep(1)
    
# Move Base 180 degree towards object
    servo1.ChangeDutyCycle(12.5)
    time.sleep(1)
    
    
#     Take Position to pick the object
    servo2.ChangeDutyCycle(3)
    time.sleep(1)
 

# open grip and close grip for pick object
    servo4.ChangeDutyCycle(.5)
    time.sleep(1)
    servo4.ChangeDutyCycle(12.5)
    time.sleep(1)
    
    
# Move to intial position and drop the object 
    servo1.ChangeDutyCycle(4)
    time.sleep(2)
    servo4.ChangeDutyCycle(.5)
    time.sleep(1)
    
    
    
    
#     back to initial
   
    
# #     Take)
#     time.sleep(1)
#     servo3.ChangeDutyCycle(10)
#     time.sleep(1)
#     servo3.ChangeDutyCycle(4)
#     time.sleep(1)
#     servo2.ChangeDutyCycle(4)
#     time.sleep(1)
# 
# 
# #     Grip Action
#     servo4.ChangeDutyCycle(2)
#     time.sleep(1)
#     servo4.ChangeDutyCycle(9)
#     time.sleep(1)
# 
# # Reverse position of servo1 and servo3
#     servo2.ChangeDutyCycle(2)
#     time.sleep(1)
#     servo3.ChangeDutyCycle(7.5)
#     time.sleep(1)
# 
# 
# # Reverse initial position of servo1(base)
#     servo1.ChangeDutyCycle(2)
#     time.sleep(1)
# # open Grip
#     servo4.ChangeDutyCycle(2)
#     time.sleep(2)


#     #Clean things up at the end
#     servo1.stop()
#     servo2.stop()
#     servo4.stop()
# 
# 
#     GPIO.cleanup()
# 
#     print ("Goodbye")
0