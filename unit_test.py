import unittest

# https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/
# Out code to be tested
class Person:

    # init method or constructor
    def __init__ (self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Jamie Morrissey')
p.say_hi()

# The test baed on unittest module  Insert a number then produce an error
class TestGetPersonClass(unittest.TestCase):
    def runTest(self):
        p = Person(1001)
        self.assertEqual(p.say_hi(), 1001, "Isn't Equal")

unittest.main()
