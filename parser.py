#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from converter import Converter

class Parser:

  def __init__(self, filename):
    self.file = open(filename, 'r')
    buffer = ''
    for line in self.file.readlines():
      line = line.strip()
      if line == '':
	  converter = Converter(buffer)
	  self.dictionary = converter.get_dictionary()
	  buffer = ''
      else:
	buffer = buffer + '\n' + line

   def get_dictionary(self):
      return self.dictionary

if __name__ == "__main__":
  parser = Parser(sys.argv[1])
  diccionario = parser.get_dictionary()
  print diccionario
