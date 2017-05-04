class FizzBuzz:

    def __init__(self, a, b):
        self.nums = list(range(a,b))
        self.fizz = []

        for i in self.nums:
            if i % 3 == 0 and i % 5 == 0:
                self.fizz.append("fizzbuzz")
            else:
                if i % 3 == 0:
                    self.fizz.append("fizz")
                elif i % 5 == 0:
                    self.fizz.append("buzz")
                else:
                    self.fizz.append(i)


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

print (fb.fizz)  #from list created during class init

for i in fb.nums:
    print (fb.fizzcheck(i)) #checking each individual number
