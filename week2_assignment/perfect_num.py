def is_perfect(n):
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n
n = 28
if is_perfect(n):
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")
