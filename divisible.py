
def divisible():
    start = int(input("start num: "))
    end = int(input("end num: "))
    print(start," == ",end)
    for i in range(start,end):
        if (i % 3 == 0) and (i % 5 == 0):
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif  i % 3 == 0:
            print("FizzBuzz")
        else:
            print(i)




divisible()