#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n + 1, i):
                    primes[j] = False
        return primes

    def simulate_game(n):
        primes = sieve_of_eratosthenes(n)
        steps = 0
        for i in range(2, n + 1):
            if primes[i]:
                steps += 1
        return steps % 2 == 1  # If odd, Maria wins; if even, Ben wins

    if x <= 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if simulate_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
