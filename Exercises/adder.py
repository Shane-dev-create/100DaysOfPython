# This is a simple addition function that returns a function that adds a number to another number.
# The function should take a number and return a function that takes another number.

def make_adder(n):
    def adder(x):
        return n + x
    return adder


addn = make_adder(3)
addx = make_adder(7)
print(addn(10))
print(addx(10))
