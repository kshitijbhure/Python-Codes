#!/usr/bin/python3

# simple fibonacci series
# the sum of two elements defines the next set
class Fibonacci():
    def __init__(self, a, b):           #constructor. Constructor defination is optional
        self.a = a
        self.b = b

    def series(self):
        while(True):
            yield(self.b)               #yield is like return
            self.a, self.b = self.b, self.a + self.b

f = Fibonacci(0, 1)             #constructor is called while object creation
for r in f.series():
    if r > 100: break
    print(r, end=' ')

