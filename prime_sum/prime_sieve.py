import math

MAX_LIMIT = 1 * 1000 * 1000 #1 million
SIEVE_CREATED = False
prime_sieve = []
limit = 15_485_863  # Approximation of the millionth prime number

def sum_prime(n):
    global SIEVE_CREATED, prime_sieve, limit
    if n > MAX_LIMIT:
        raise Exception(f"Not Implemented for primes larger than {MAX_LIMIT}")
    
    if not SIEVE_CREATED:
        prime_sieve = [True] * limit
        prime_sieve[0] = prime_sieve[1] = False
        SIEVE_CREATED = True

    prime_sum = 0
    count = 0

    for num in range(2, limit):
        if prime_sieve[num]:
            prime_sum += num
            count += 1
            if count == n:
                break
            for multiple in range(num * num, limit, num):
                prime_sieve[multiple] = False
    return prime_sum

def reset_sieve():
    global SIEVE_CREATED, prime_sieve, limit
    SIEVE_CREATED = False
    prime_sieve = []

if __name__ == '__main__':
    sum_of_primes = sum_prime(1000000)
    print("Sum of the first million prime numbers:", sum_of_primes)
