import snoop
from contextlib import contextmanager

@snoop.snoop()
def main():
    x = (
        [
            bar(),  # 1
            bar(),  # 2
        ]
    )

    with context(
            bar(),  # 1
            bar(),  # 2
    ):
        try:
            for _ in [
                bar(
                    bar(),  # 1
                    bar(),  # 2
                )
            ]:
                while bar(
                        bar(),  # 1
                        bar(),  # 2
                ):
                    pass
                else:
                    bar()
            else:
                bar()
                raise ValueError
        except (
                ValueError,
                TypeError,
        ):
            pass
        finally:
            bar(
                [
                    bar(),  # 1
                    bar(),  # 2
                ]
            )

    with context(
            bar(),  # 1
            bar(),  # 2
    ):
        if bar(
                bar(),  # 1
                bar(),  # 2
        ):
            pass
        elif [
            bar(
                bar(),  # 1
                bar(),  # 2
            )
        ]:
            pass
        
    return x


def bar(*_):
    pass


@contextmanager
def context(*_):
    yield


expected_output = """
12:34:56.78 >>> Call to main in File "/path/to_file.py", line 5
12:34:56.78    5 | def main():
12:34:56.78    6 |     x = (
12:34:56.78    7 |         [
12:34:56.78    8 |             bar(),  # 1
12:34:56.78    9 |             bar(),  # 2
12:34:56.78 .......... x = [None, None]
12:34:56.78 .......... len(x) = 2
12:34:56.78   13 |     with context(
12:34:56.78   14 |             bar(),  # 1
12:34:56.78   15 |             bar(),  # 2
12:34:56.78   17 |         try:
12:34:56.78   18 |             for _ in [
12:34:56.78   19 |                 bar(
12:34:56.78   20 |                     bar(),  # 1
12:34:56.78   21 |                     bar(),  # 2
12:34:56.78 .................. _ = None
12:34:56.78   24 |                 while bar(
12:34:56.78   25 |                         bar(),  # 1
12:34:56.78   26 |                         bar(),  # 2
12:34:56.78   30 |                     bar()
12:34:56.78   18 |             for _ in [
12:34:56.78   19 |                 bar(
12:34:56.78   20 |                     bar(),  # 1
12:34:56.78   21 |                     bar(),  # 2
12:34:56.78   32 |                 bar()
12:34:56.78   33 |                 raise ValueError
12:34:56.78 !!! ValueError
12:34:56.78   34 |         except (
12:34:56.78   35 |                 ValueError,
12:34:56.78   36 |                 TypeError,
12:34:56.78   38 |             pass
12:34:56.78   40 |             bar(
12:34:56.78   42 |                     bar(),  # 1
12:34:56.78   43 |                     bar(),  # 2
12:34:56.78   47 |     with context(
12:34:56.78   48 |             bar(),  # 1
12:34:56.78   49 |             bar(),  # 2
12:34:56.78   51 |         if bar(
12:34:56.78   52 |                 bar(),  # 1
12:34:56.78   53 |                 bar(),  # 2
12:34:56.78   56 |         elif [
12:34:56.78   57 |             bar(
12:34:56.78   58 |                 bar(),  # 1
12:34:56.78   59 |                 bar(),  # 2
12:34:56.78   62 |             pass
12:34:56.78   64 |     return x
12:34:56.78 <<< Return value from main: [None, None]
"""
