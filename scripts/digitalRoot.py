def digital_root(n):
    m = str(n)
    converted = list(m)
    numbers = [int(x) for x in converted]
    return sum(numbers)

print (digital_root(27))
