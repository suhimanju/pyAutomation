"""
Program that iterates through loop between [1 to 100] and prints "fizz" if divisible by 3,
prints "buzz" if divisible by 5, divisible by 3 & 5, print “fizzbuzz”
"""

for i in range(1,100):
    if((i%3)==0 and(i%5)==0):
        print("Its a: fizzbuzz")

    elif((i%3)==0):
        print("Its a: fizz")

    elif(i%5)==0:
        print("Its a: buzz")
