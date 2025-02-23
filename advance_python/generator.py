def infinite_generator():
    result = 1
    while True:
        yield result
        result *= 2
        
values = infinite_generator()

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))