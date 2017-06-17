#!/usr/bin/env python

''' fgdgd '''
import unittest

from buzz import generator

def test_sample_single_word():
    l = ('foo', 'bar', 'foobar')
    word = generator.sample(l)
    assert word in l
