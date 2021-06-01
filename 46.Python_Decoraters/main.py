import time


# time.time returns the current time in seconds since January 1, 1970, 00:00:00

# This Decorator calculates the time taken for a function to run
def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        print(f"The Start Time: {start_time}")
        function()
        end_time = time.time()
        print(f"The End Time: {end_time}")
        print(f"The total time taken: {end_time - start_time}")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
