#!/usr/bin/env python

def processor(reader, converter, writer):
  while True:
    data = reader.read()
    if not data:
      break
    data = converter(data)
    writer.write(data)

class Processor:
  def __init__(self, reader, writer):
    self.reader = reader
    self.writer = writer

  def process(self):
    while True:
      data = self.reader.readline()
      if not data:
        break
      data = self.converter(data)
      self.writer.write(data)

  def converter(self, data):
    assert False, 'Define me!!!'


if __name__ == '__main__':
    print "Self Testing"
