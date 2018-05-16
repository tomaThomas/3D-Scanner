import gpio

startPin = 22

print("Init stepper")

def rotate(degrees):
    print("rotating " + str(degrees) + "°")

def step():
    print("moving step")

gpio.init(startPin)
