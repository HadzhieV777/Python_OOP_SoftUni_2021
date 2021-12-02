# 05. Cache

def cache(func):
    log = {}

    def wrapper(n):
        if not n in log:
            log[n] = func(n)
            return log[n]
        return log[n]

    wrapper.log = log

    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)
