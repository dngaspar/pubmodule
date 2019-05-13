import pysnooper


def f2(a):
    def f3(a):
        x = 0
        x += 1

        def f4(_a):
            _y = x
            return 42

        return f4(a)

    return f3(a)


def main():
    with pysnooper.snoop(depth=4):
        result1 = f2(42)
    return result1


expected_output = """
12:34:56.789012 line        20         result1 = f2(42)
Starting var:.. a = 42
12:34:56.789012 call         4 def f2(a):
12:34:56.789012 line         5     def f3(a):
New var:....... f3 = <function f2.<locals>.f3 at 0xABC>
12:34:56.789012 line        15     return f3(a)
    Starting var:.. a = 42
    12:34:56.789012 call         5     def f3(a):
    12:34:56.789012 line         6         x = 0
    New var:....... x = 0
    12:34:56.789012 line         7         x += 1
    Modified var:.. x = 1
    12:34:56.789012 line         9         def f4(_a):
    New var:....... f4 = <function f2.<locals>.f3.<locals>.f4 at 0xABC>
    12:34:56.789012 line        13         return f4(a)
        Starting var:.. _a = 42
        Starting var:.. x = 1
        12:34:56.789012 call         9         def f4(_a):
        12:34:56.789012 line        10             _y = x
        New var:....... _y = 1
        12:34:56.789012 line        11             return 42
        12:34:56.789012 return      11             return 42
        Return value:.. 42
    12:34:56.789012 return      13         return f4(a)
    Return value:.. 42
12:34:56.789012 return      15     return f3(a)
Return value:.. 42
"""