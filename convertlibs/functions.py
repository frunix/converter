__author__ = "Frederik Gowy"  

"""
functions to be used in combinations with the convertlib classes
"""

from temperature import Temperature
from lenght import Lenght

# Temperature functions

def printtemperature(temp, unit):
  print 'Temperature is', temp, unit

def processtemp(amount, inputunit, outputunit):
  degrees = Temperature(temperature=amount, system=inputunit)

  if outputunit == 'celsius':
    printtemperature(temp=degrees.celsius(), unit=outputunit)
  elif outputunit == 'fahrenheit':
    printtemperature(temp=degrees.fahrenheit(), unit=outputunit)
  elif outputunit == 'kalvin':
    printtemperature(temp=degrees.kalvin(), unit=outputunit)
  elif outputunit == 'rankine':
    printtemperature(temp=degrees.rankine(), unit=outputunit)

