from pysnooper import snoop, pp


@snoop()
def main():
    x = 1
    y = 2
    pp(pp(x + 1) + max(*pp(y + 2, y + 3)))


expected_output = """
12:34:56.78 >>> Call to main in pp.py
12:34:56.78    5 | def main():
12:34:56.78    6 |     x = 1
12:34:56.78    7 |     y = 2
12:34:56.78    8 |     pp(pp(x + 1) + max(*pp(y + 2, y + 3)))
12:34:56.78 LOG:
12:34:56.78 .... x + 1 = 2
12:34:56.78 LOG:
12:34:56.78 .... y + 2 = 4
12:34:56.78 .... y + 3 = 5
12:34:56.78 LOG:
12:34:56.78 .... pp(x + 1) + max(*pp(y + 2, y + 3)) = 7
12:34:56.78 <<< Return value from main: None
"""
