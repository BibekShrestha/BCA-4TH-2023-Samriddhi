
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_prime_inefficient(n):
    if n <= 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def sum_primes_better(n):
    count = 0
    num = 2
    prime_sum = 0
    while count < n:
        if is_prime(num):
            prime_sum += num
            count += 1
            
        num += 1
    return prime_sum

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
    


if __name__ == '__main__':
    sum_of_primes = sum_primes_better(1000000)
    print("Sum of the first million prime numbers:", sum_of_primes)
