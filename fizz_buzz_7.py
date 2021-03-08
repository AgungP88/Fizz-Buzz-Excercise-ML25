import itertools

fizzes = itertools.cycle(["", "", "fizz"])
buzzes = itertools.cycle(["", "", "", "", "buzz"])
numbers = itertools.count(1)

fizz_buzzes = (
    (fizz + buzz) or n
    for fizz, buzz, n in zip(fizzes, buzzes, numbers))

print([next(fizz_buzzes)
 for _ in range(100)])
