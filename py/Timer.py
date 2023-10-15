from time import perf_counter_ns

def time_this(func):
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        func(*args, *kwargs)
        end = perf_counter_ns()
        print(f'{func.__name__} executed in {end-start} ns')
    return wrapper