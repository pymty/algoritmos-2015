def fib(n):
    if n <= 0:
        return 0
    i = n - 1
    (a, b) = (1, 0)
    (c, d) = (0, 1)
    while i > 0:
        if i % 2:
            (a, b) = (d * b + c * a,  d * (b + a) + c * b)
        (c, d) = (c * c + d * d, d * (2 * c + d))
        i = i / 2
    return a + b

def main():
    print fib(10)

main()
