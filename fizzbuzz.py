for x in xrange (101):
    if x % 3 == 0 and x % 5 == 0:
        print "fizzbuzz"
    else:
        if x % 3 == 0:
            print "fizz"
        elif x % 5 == 0:
            print "buzz"
        else:
            print x
