import RPi.GPIO as GPIO
import time
import os

GPIO_PIN = 26 #sensor pin define

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN,GPIO.IN)


def loop():
    while True:
        if(GPIO.input(GPIO_PIN)==GPIO.HIGH):
            print("反応あり！")
            time.sleep(1)
        else:
            print("反応なし")
            time.sleep(1)
            
def destroy():
    GPIO.cleanup()

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()