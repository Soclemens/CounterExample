x = 1
foundNonPrime = False
while not foundNonPrime:
    num = (x ** 2) + x + 41

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(x, " creates a non prime number at ", num)
                foundNonPrime = True
    x += 1
