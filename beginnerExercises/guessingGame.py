import random

a = random.randint(0, 9)

print("I'm thinking of a number between one and ten...take a guess?")
user = int(input("Your guess: "))
print(f'My number is {a}')


if user == a:
    print("You're exactly right!")
elif user > a:
    print("Sorry - too high!")
else:
        print("Sorry - too low!")