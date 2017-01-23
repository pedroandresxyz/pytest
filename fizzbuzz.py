class FizzBuzz:

    def __init__(self, a, b):
        self.nums = list(range(a,b))

    def fizzcheck(self, x):
        if x % 3 == 0 and x % 5 == 0:
            return "fizzbuzz"
        else:
            if x % 3 == 0:
                return "fizz"
            elif x % 5 == 0:
                return "buzz"
            else:
                return x


fb = FizzBuzz(1,101)

for i in fb.nums:
    print fb.fizzcheck(i)
