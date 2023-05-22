import argparse
import prime_brute
import prime_sieve


def parse_arguments():
    parser = argparse.ArgumentParser("Sum Primes", description=" Calculate sum of prime number up to given number")
    parser.add_argument("-c", "--count", type=int, default=10000000)
    parser.add_argument("-a", "--algorithm", choices=['brute', 'better', 'sieve'], default='brute')
    return parser.parse_args()
    
def main():
    args = parse_arguments()
    prime_count = args.count
    print(f"Finding sum of first {prime_count} primes")
    print(f"Using algorithm : {args.algorithm}")
    if args.algorithm == 'brute':
        sum_of_primes = prime_brute.sum_primes_brute(prime_count)
    elif args.algorithm == 'better':
        sum_of_primes = prime_brute.sum_primes_better(prime_count)
    elif args.algorithm == 'sieve':
        sum_of_primes = prime_sieve.sum_prime(prime_count)
    else:
        raise NotImplementedError

    print(f"Sum of the first {prime_count} prime numbers: {sum_of_primes}")


if __name__ == '__main__':
    main()
