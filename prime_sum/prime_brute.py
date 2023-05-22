def is_prime_inefficient(n):
    if n <= 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def sum_primes_brute(n):
    count = 0
    num = 2
    prime_sum = 0
    while count < n:
        if is_prime_inefficient(num):
            prime_sum += num
            count += 1   
        num += 1
    return prime_sum
    
