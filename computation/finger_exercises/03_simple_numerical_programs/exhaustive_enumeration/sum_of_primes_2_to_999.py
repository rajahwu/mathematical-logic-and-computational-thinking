def is_prime(num):
    if num < 2:
        return False
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True

def sum_of_primes_2_to_999():
    total = 0
    for num in range(2, 1000):
        if is_prime(num):
            total += num
    return total

print(sum_of_primes_2_to_999())  # 76127