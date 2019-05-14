import pysnooper


def f4(x4):
    result4 = x4 * 2
    return result4


def f3(x3):
    result3 = f4(x3)
    return result3


def f2(x2):
    result2 = f3(x2)
    return result2


def main():
    str(3)
    with pysnooper.snoop(depth=3):
        result1 = f2(5)
    return result1


expected_output = """
12:34:56.78 line        22         result1 = f2(5)
........... x2 = 5
12:34:56.78 call        14 def f2(x2):
12:34:56.78 line        15     result2 = f3(x2)
    ........... x3 = 5
    12:34:56.78 call         9 def f3(x3):
    12:34:56.78 line        10     result3 = f4(x3)
    ........... result3 = 10
    12:34:56.78 line        11     return result3
    <<< Return value from f3: 10
........... result2 = 10
12:34:56.78 line        16     return result2
<<< Return value from f2: 10
"""
