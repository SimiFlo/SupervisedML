import random
import numpy as np
from datetime import datetime
from tkinter import *
import time

# activation function
def sign(n):
    if n >= 0:
        return 1
    else:
        return -1

class Point(object):

    def __init__(self):
        random.seed()
        self.x = random.randint(10, 490)
        self.y = random.randint(10, 490)
        self.label = None

    def X(self):
        return self.x

    def Y(self):
        return self.y

    def Label(self):
        if self.x > self.y:
            return 1
        else:
            return -1

class Percepton(object):

    def __init__(self):
        self.sum = 0
        np.random.seed()
        # randomly assign weights
        self.weights = np.random.randint(-1,1,2)

    # guess function that takes into account the weight and associated input and will use the activation function
    # to assign a value to the percepton value
    def guess(self, input_data):
        self.sum = 0
        for i in range(len(self.weights)):
            self.sum += self.weights[i] * input_data[i]
        #print(self.sum)
        return sign(self.sum)

    # trains the perceptor based on the input
    def train(self, input_data, target):
        guess = self.guess(input_data)
        error = target - guess

        # tuning it with a learning rate of 10%
        for i in range(len(self.weights)):
            self.weights[i] += error * input_data[i] * 0.1
            print(self.weights[i])

def populateArray(pointArray):
    for i in range(125):
        point = Point()
        pointArray.append(point)
    return pointArray

if __name__ == '__main__':
    p = Percepton()
    pointArray = []
    pointArray = populateArray(pointArray)

    root = Tk()
    c = Canvas(root, width=500, height=500)
    c.pack()

    input_data = []

    # initial display
    for i in range(len(pointArray)):
        input_data.clear()
        input_data.append(pointArray[i].X())
        input_data.append(pointArray[i].Y())
        guess = p.guess(input_data)
        label = 'red'
        if guess == pointArray[i].Label():
            label = 'green'
        c.create_oval(pointArray[i].X(), pointArray[i].Y(), pointArray[i].X() + 15, pointArray[i].Y() + 15,
                      fill=label)
    root.update()
    time.sleep(1)

    # training session
    for i in range(5):
        for i in range(len(pointArray)):
            input_data.clear()
            input_data.append(pointArray[i].X())
            input_data.append(pointArray[i].Y())
            p.train(input_data, pointArray[i].Label())
            guess = p.guess(input_data)
            label = 'red'
            if guess == pointArray[i].Label():
                label = 'green'
            c.create_oval(pointArray[i].X(), pointArray[i].Y(), pointArray[i].X() + 15, pointArray[i].Y() + 15,
                          fill=label)

    root.update()
    time.sleep(1)

    root.mainloop()
