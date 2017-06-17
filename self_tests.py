#!/usr/bin/env python

import math

''' Interview practice...'''

def factorial(n):
    res = 1
    for i in range(n):
        res *= i + 1
    return res

def fibonacchi(n):
    a = b = 1
    for i in range(n-1):
        a,b = b,a+b
    return a

def fibonacchi2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacchi2(n-2) + fibonacchi2(n-1)

def is_prime(n, trace=False):
    m = int(math.sqrt(n)) + 1
    while m > 1:
        if n % m == 0:
            if trace: print '{0} has the factor {1}'.format(n, m)
            return False
        m -= 1

    return True

def prime_factors(n):
    factors = []
    m = 2
    while m <= int(math.sqrt(n)) + 1:
        if n % m == 0:
            factors.append(m)
            n //= m
        else:
            m += 1

    if n > 1:
        factors.append(n)

    return factors

def is_anagram(word1, word2):
    w1 = word1.lower().replace(' ', '')
    w2 = word2.lower().replace(' ', '')
    l = list(w2)
    for ch in w1:
        if ch in l:
            l.remove(ch)

    return len(l) == 0


if __name__ == '__main__':
    print 'Self Testing...'

    print '{0}! = {1}'.format(6, factorial(6))

    print 'fib({0}) = {1}'.format(8, fibonacchi(8))
    print 'fib2({0}) = {1}'.format(8, fibonacchi2(8))

    print 'Is {0} prime? {1}'.format(83, is_prime(83))
    print 'Is {0} prime? {1}'.format(343, is_prime(343, trace=True))

    word1 = 'Stop'
    word2 = 'Pots'
    word3 = 'top'
    print 'Are {0} and {1} anagrams? {2}'.format(word1, word2, is_anagram(word1, word2))
    print 'Are {0} and {1} anagrams? {2}'.format(word3, word2, is_anagram(word3, word2))


    print 'Prime factors of {0}: {1}'.format(1280, prime_factors(1280))
    print 'Prime factors of {0}: {1}'.format(49, prime_factors(49))
    print 'Prime factors of {0}: {1}'.format(83, prime_factors(83))
