x = 645976

def sqrt(x):
    for i in range(x):
        if i ** 2 > x:
            return i - 1

print(sqrt(x))