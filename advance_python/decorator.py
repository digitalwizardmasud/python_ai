# def decorator(function):
#     def wrapper(*args, **kwargs):
#         function(*args, **kwargs)
#         print("I am decorating your function")
#     return wrapper


# def hello_world(person):
#     print(f"hello {person}")

# decorated = decorator(hello_world)
# decorated("Alice")

import time
import random
def logger(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        val = function(*args, *kwargs)
        after = time.time()
        with open("logfile.txt", "a+") as f:
            output = f"{function.__name__} returned value {val} and execution time= {int(after - before)}s\n"
            print(output)
            f.write(output)
    return wrapper

@logger
def add(x, y):
    time.sleep(random.randint(1,5))
    return x + y

add(10, 20)
add(12, 20)

@logger
def mul(x, y):
    time.sleep(random.randint(1,5))
    return x * y

mul(10, 20)
mul(12, 20)
