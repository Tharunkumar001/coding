for i in range(1,100):
    inpu = int(input("Enter a number \n"))
    if (inpu % 3 == 0 and inpu % 5 == 0):
        print("fizzbuzz")
    elif (inpu % 5 == 0):
        print("buzz")
    elif (inpu % 3 == 0):
        print("fizz")

