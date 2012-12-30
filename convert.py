#!/usr/bin/python


"""
Converts
Read README.txt
"""

__author__ = "Frederik Gowy"

import sys
import re
from convertlibs.functions import * 

args = sys.argv[1:]
argscorrect = re.search(r'^\w* \d* \w* to \w*', ' '.join(args))

if not argscorrect:
  print 'wrong/missing arguments'
  exit(1)

subject = args[0]
amount = args[1]
inputunit = args[2]
outputunit = args[4]

# check wether I need to output some basic DEBUG info with debugoutput() or not
try:
  enabledebug = args[5]
except IndexError:
  enabledebug = 'null'

def debugoutput():
  print '\n\n--DEBUG-------------'
  print 'subject: ', subject
  print 'amount: ', amount
  print 'inputunit: ', inputunit
  print 'outputunit: ', outputunit
  print '------------------------\n\n'

def main():
  # if debug is given as extra argument, return some basic reads from the
  # argument line
  if enabledebug == 'debug':
    debugoutput()

  # actual programm
  if subject == 'temp' or subject == 'temperature':
    processtemp(amount, inputunit, outputunit)
  else:
    print subject, 'not supported (yet?)'


if __name__ == '__main__':
  main()
