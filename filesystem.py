#!/usr/bin/env python

'''
Various file system utils, part of my learning experience
'''

import os, sys
import glob
import argparse

def lister(dir, indent=''):
    if len(indent) == 0:
        print '{0}{1}{2}:'.format(indent, dir, os.sep)

    indent += '  '

    # base case - print files
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if os.path.isfile(path):
            print '{0}{1}'.format(indent, file)

    # recurse case - dirs
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if os.path.isdir(path):
            print '{0}{1}{2}:'.format(indent, file, os.sep)
            lister(path, indent)

def walker(dir):
    for (dirname, dirs, files) in os.walk(dir):
        print '{0}{1}:'.format(dirname, os.sep)
        for file in files:
            if file.endswith('.py'):
              print '  {0}'.format(file)



def main():
    parser = argparse.ArgumentParser(description='Various dir tree workings')
    parser.add_argument('-w', '--welcome', action='store_true', dest='welcome', help='Print a welcome message')
    parser.add_argument('-r', action='store', dest='root', default = '/Users/andy/dev/python/tests', help='Root directory for photo analysis')
    parser.add_argument('-l', action = 'store', type=int, dest='limit', help='Limiting output')
    args = parser.parse_args()

    if args.welcome:
        print 'Welcome to ', sys.argv[0], '!!!'
        parser.print_usage()

    if args.limit:
        print 'TODO, add some sort of output limit ', args.limit

    root = args.root

    print '-' * 48
    print 'RECURSIVE:'
    lister(root)

    print '-' * 48
    print 'WALKER:'
    walker(root)

    # Analyse photos
    trace = False
    #root = '/Users/andy/Pictures/Lightroom Photos/House'
    root = args.root
    results = {}
    print 'Scanning ', root
    for (dirname, dirs, files) in os.walk(root):
        if trace: print '{0}{1}:'.format(dirname, os.sep)
        for file in files:
            extension = file.split('.')[-1]
            if results.has_key(extension):
                results[extension] += 1
            else:
                results[extension] = 1

    for key in results.keys():
        print '  *.{0:<10}: {1:5d}'.format(key, results[key])


if __name__ == '__main__':
    main()
