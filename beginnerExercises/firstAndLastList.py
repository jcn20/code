def numbers(a):
    if isinstance(a, list):
        return [a[0], a[-1]]


print(numbers([1, 2, 3, 4]))
