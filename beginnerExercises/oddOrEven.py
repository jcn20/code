# Challenge: http://www.practicepython.org

def odd_or_even(num, check):  # Main problem
    if num % 2 == 0 and num % 4 == 0:
        print("Not only is this number even: it's divisible by 4.")
    elif num % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd.")
    if num % check == 0:
        print("Your number can be divided evenly by the 'check' number"
              " you provided.")
    elif num % check != 0:
        print("Sorry, your two arguments are not evenly divisible by each other.")


num = int(input("Give me a number: "))
check = int(input("Give me a number to check and see if it's evenly"
                  " divisible by the 'num' you supplied:  "))
odd_or_even(num, check)
