import RPi.GPIO as GPIO

firstPin = -10
out = [False, False, False, False]

def init(startPin):
    global firstPin
    firstPin = startPin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(firstPin, GPIO.OUT)
    GPIO.setup(firstPin + 1, GPIO.OUT)
    GPIO.setup(firstPin + 2, GPIO.OUT)
    GPIO.setup(firstPin + 3, GPIO.OUT)

def setGPIOs(a, b, c, d):
    global out
    out = [a, b, c, d]
    GPIO.output(firstPin, a)
    GPIO.output(firstPin + 1, b)
    GPIO.output(firstPin + 2, c)
    GPIO.output(firstPin + 3, d)

def toggle(pin):
    global out
    out[pin] = not out[pin]
    GPIO.output(pin + firstPin, out[pin])
