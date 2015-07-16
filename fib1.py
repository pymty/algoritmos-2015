def main():
    n = 10
    phi = (1.0 + (5.0 ** 0.5)) / 2.0
    fn = ((phi ** n) - ((1.0 - phi) ** n)) / (5.0 ** 0.5)
    print fn

main()
