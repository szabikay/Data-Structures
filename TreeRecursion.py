def calculate(n):
    if n > 0:
        calculate(n - 5)
        k = n ** 2
        print(k)
        calculate(n - 5)

calculate(15)
