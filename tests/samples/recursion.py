import pysnooper


@pysnooper.snoop(depth=2)
def factorial(x):
    if x <= 1:
        return 1
    return mul(x, factorial(x - 1))


def mul(a, b):
    return a * b


def main():
    factorial(4)
    
expected_output = """
12:34:56.78 >>> Call to factorial in recursion.py
12:34:56.78 ...... x = 4
12:34:56.78    5 | def factorial(x):
12:34:56.78    6 |     if x <= 1:
12:34:56.78    8 |     return mul(x, factorial(x - 1))
    12:34:56.78 >>> Call to factorial in recursion.py
    12:34:56.78 ...... x = 3
    12:34:56.78    5 | def factorial(x):
    12:34:56.78    6 |     if x <= 1:
    12:34:56.78    8 |     return mul(x, factorial(x - 1))
        12:34:56.78 >>> Call to factorial in recursion.py
        12:34:56.78 ...... x = 2
        12:34:56.78    5 | def factorial(x):
        12:34:56.78    6 |     if x <= 1:
        12:34:56.78    8 |     return mul(x, factorial(x - 1))
            12:34:56.78 >>> Call to factorial in recursion.py
            12:34:56.78 ...... x = 1
            12:34:56.78    5 | def factorial(x):
            12:34:56.78    6 |     if x <= 1:
            12:34:56.78    7 |         return 1
            12:34:56.78 <<< Return value from factorial: 1
            12:34:56.78 >>> Call to mul in recursion.py
            12:34:56.78 ...... a = 2
            12:34:56.78 ...... b = 1
            12:34:56.78   11 | def mul(a, b):
            12:34:56.78   12 |     return a * b
            12:34:56.78 <<< Return value from mul: 2
        12:34:56.78 <<< Return value from factorial: 2
        12:34:56.78 >>> Call to mul in recursion.py
        12:34:56.78 ...... a = 3
        12:34:56.78 ...... b = 2
        12:34:56.78   11 | def mul(a, b):
        12:34:56.78   12 |     return a * b
        12:34:56.78 <<< Return value from mul: 6
    12:34:56.78 <<< Return value from factorial: 6
    12:34:56.78 >>> Call to mul in recursion.py
    12:34:56.78 ...... a = 4
    12:34:56.78 ...... b = 6
    12:34:56.78   11 | def mul(a, b):
    12:34:56.78   12 |     return a * b
    12:34:56.78 <<< Return value from mul: 24
12:34:56.78 <<< Return value from factorial: 24
"""
