import RPi.GPIO as GPIO

firstPin = None

def init(startPin):
    global firstPin
    firstPin = startPin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(firstPin, GPIO.OUT)
    GPIO.setup(firstPin + 1, GPIO.OUT)
    GPIO.output(firstPin, False)
    GPIO.output(firstPin + 1, False)

def set(pin, value):
    GPIO.output(pin + firstPin, value)

def cleanup():
    GPIO.cleanup()
