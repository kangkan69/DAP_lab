def singleDigit(n):
    sum = 0
    while n > 0 or sum > 9:
        if n == 0:
            n = sum
            sum = 0

        sum += n % 10
        n //= 10
    return sum

if __name__ == "__main__":
    n = 1234
    print(singleDigit(n))
