def func1(a, b):
    return a / b

def func2(x):
    a = x
    b = x - 1
    return func1(a, b)

for val in range(5, 1, -1):
    func2(val)
