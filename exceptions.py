#!/usr/bin/env python

def kaboom(a,b):
  print(a + b)

try:
  kaboom('b',2)
except TypeError:
  print('Not good')
else:
  print('It worked')
finally:
  print('Goodnight!!')

sep = '_' * 72

print(sep)
print('Resuming...')
