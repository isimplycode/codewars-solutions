memoi = {}
def fibonacci(n):
    if n in [0, 1]:
        return n
    if n in memoi:
        return memoi[n]
    memoi[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci(n - 1) + fibonacci(n - 2)
