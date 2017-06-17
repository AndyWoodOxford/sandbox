#!/usr/bin/env python

import itertools
import math
import os

''' Basic algorithms '''

def factorial(n):
    result = 1
    for i in range(n):
        result *= i+1
    return result

def facr(n):
    # base case
    if n == 1:
        return 1

    # recurse case
    return n * facr(n-1)

def fibonacci(n):
    a = b = 1
    for i in range(n-2):
        a,b = b,a+b
    return b

def fibonacci2(n):
    # base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # recurse case
    return fibonacci2(n-2) + fibonacci2(n-1)

def is_prime(n):
    m = int(math.sqrt(n)) + 1
    while m > 1:
        if n % m == 0:
            print 'FALSE - {0} has a factor {1}'.format(n, m)
            return False
        m -= 1
    print 'TRUE - {0} is prime'.format(n)
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

    w2l = list(w2)
    for ch in w1:
        if ch not in w2l:
            return False
        else:
            w2l.remove(ch)

    return len(w2l) == 0

def file_system_walker(dir, indent=''):
    print '{0}{1}{2}:'.format(indent, dir, os.sep)
    for file in os.listdir(dir):
        if file == '.git':
            print 'Skipping .git directory'
            continue

        path = os.path.join(dir, file)
        if os.path.isfile(path):
            print '{0}{1}'.format(indent, file)
        elif os.path.isdir(path):
            indent += '  '
            file_system_walker(path, indent)
        else:
            print 'ERROR unknown file type: ', file


def merge(lhs, rhs):
    result = []
    while len(lhs) > 0 and len(rhs) > 0:
        if lhs[0] < rhs[0]:
            result.append(lhs[0])
            lhs.remove(lhs[0])
        else:
            result.append(rhs[0])
            rhs.remove(rhs[0])

    if len(lhs) > 0:
        result += lhs
    else:
        result += rhs

    return result

def merge_sort(mylist):
    # Base case - reduced to single element
    if len(mylist) == 1:
        return mylist

    # Recurse case - split into (approximate) halves and merge these
    midpoint = len(mylist) / 2
    lhs = merge_sort(mylist[:midpoint])
    rhs = merge_sort(mylist[midpoint:])

    return merge(lhs, rhs)

def bubble_sort(mylist):
    # outer loop - number of passes
    for i in range(len(mylist)-1, 0, -1):
        # inner loop - number of elements to compare
        for j in range(i):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1],mylist[j]
    print 'Bubble sorted: ', mylist


def combos(s):
    l = list(itertools.permutations(s, len(s)))
    result = []
    for ch in range(len(l)):
        result.append(''.join(l[ch]))
    return result


if __name__ == '__main__':
    print 'Self Testing'

    print 'Factorial 5: ', factorial(5)
    print 'Factorial 0: ', factorial(0)
    print 'Factorial -3: ', factorial(-3)

    print 'Recursive Factorial 5:', facr(5)

    print 'Fibonacci:'
    print 'Fib 10: ', fibonacci(10)
    print 'Fib 1: ', fibonacci(1)
    print 'Fib 0: ', fibonacci(0)

    print 'Fib2 10: ', fibonacci2(10)
    print 'Fib2 1: ', fibonacci2(1)
    print 'Fib2 0: ', fibonacci2(0)

    print 'Primes:'
    is_prime(47)
    is_prime(1005)

    print 'Prime factors:'
    print '16 ', prime_factors(16)
    print '1005: ', prime_factors(1005)
    print '47: ', prime_factors(47)

    print 'Anagrams:'
    w1 = 'Alec Guinness'
    w2 = 'Genuine Class'
    w3 = 'Alec'
    print 'Are \'{0}\' and \'{1}\' anagrams? {2}'.format(w1, w2, is_anagram(w1,w2))
    print 'Are \'{0}\' and \'{1}\' anagrams? {2}'.format(w1, w3, is_anagram(w1,w3))

    print 'Lists:'
    l = list('Hello World')
    print 'Merge Sorted: %s' % (merge_sort(l))
    bubble_sort(l)

    print 'Dir Walker'
    #print file_system_walker('/Users/andy/dev/python/ci_sample')

    print 'Letter combinations'
    print 'ABC: ', combos('abc')
    print 'DD: ', combos('dd')
