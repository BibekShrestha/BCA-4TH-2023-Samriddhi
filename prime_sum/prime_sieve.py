import math

MAX_LIMIT = 1 * 1000 * 1000 #1 million

import math

def estimate_nth_prime(n):

    if n < 25:
        #primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97, 101]
        return 105
    upper_bound = math.ceil(n * (math.log(n) + math.log(math.log(n)) - 1 + 1.8 * math.log(math.log(n)) / math.log(n)))

    if n > 8601:
        upper_bound = math.ceil(n * (math.log(n) + math.log(math.log(n)) - 0.9385))
    return upper_bound

def sum_prime(n):
    if n > MAX_LIMIT:
        raise Exception(f"Not Implemented for primes larger than {MAX_LIMIT}")
    current_limit = estimate_nth_prime(n)
    prime_sieve = [True] * current_limit
    prime_sieve[0] = prime_sieve[1] = False

    prime_sum = 0
    count = 0

    for num in range(2, current_limit):
        if prime_sieve[num]:
            prime_sum += num
            count += 1
            if count == n:
                break
            for multiple in range(num * num, current_limit, num):
                prime_sieve[multiple] = False
    return prime_sum

def reset_sieve():
    global SIEVE_CREATED, prime_sieve, limit
    SIEVE_CREATED = False
    prime_sieve = []

if __name__ == '__main__':
    sum_of_primes = sum_prime(1000000)
    print("Sum of the first million prime numbers:", sum_of_primes)
