def fibonacci_of(f):
    if f in {0, 1}:
        return f
    return fibonacci_of(f-1) + fibonacci_of(f - 2)
    
sequence = [fibonacci_of(f) for f in range (12)]
print(sequence)

input ()
