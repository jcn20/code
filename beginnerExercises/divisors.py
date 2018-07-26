def divisors(x):
    new_list = []
    lst = range(1, x+1)
    for i in lst:
        if x % i == 0:
            new_list.append(i)
    print(new_list)


x = int(input("Give me a number: "))

divisors(x)
