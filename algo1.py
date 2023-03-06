# algorithmic complexity and big O notation

# Explain all the notations and complexities

# O(1) - constant time - the time it takes to run the algorithm is constant regardless of the size of the input. The algorithm will always take the same amount of time to run. 

# O(n) - linear time - the time it takes to run the algorithm is directly proportional to the size of the input. The algorithm will take longer to run as the input size increases. 

# O(n^2) - quadratic time - the time it takes to run the algorithm is proportional to the square of the size of the input. The algorithm will take longer to run as the input size increases.

# O(2^n) - exponential time - the time it takes to run the algorithm is proportional to 2 to the power of the size of the input. The algorithm will take longer to run as the input size increases.

# O(n!) - factorial time - the time it takes to run the algorithm is proportional to the factorial of the size of the input. The algorithm will take longer to run as the input size increases.

# O(log n) - logarithmic time - the time it takes to run the algorithm is proportional to the logarithm of the size of the input. The algorithm will take longer to run as the input size increases.

# O(n log n) - linearithmic time - the time it takes to run the algorithm is proportional to the size of the input times the logarithm of the size of the input. The algorithm will take longer to run as the input size increases.

# O(1) - constant time
def constant_time(n):
    return n[0]

# O(n) - linear time
def linear_time(n):
    for i in n:
        print(i)

# O(n^2) - quadratic time
def quadratic_time(n):
    for i in n:
        for j in n:
            print(i, j)

# O(2^n) - exponential time
def exponential_time(n):
    if n <= 1:
        return n
    else:
        return exponential_time(n-1) + exponential_time(n-1)

# O(n!) - factorial time
def factorial_time(n):
    if n <= 1:
        return n
    else:
        return n * factorial_time(n-1)

# O(log n) - logarithmic time
def logarithmic_time(n):
    if n <= 1:
        return n
    else:
        return logarithmic_time(n/2)

# O(n log n) - linearithmic time
def linearithmic_time(n):
    if n <= 1:
        return n
    else:
        return logarithmic_time(n/2) + linearithmic_time(n/2)

