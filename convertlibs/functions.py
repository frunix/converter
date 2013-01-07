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

def printlenght(amount, unit):
  print 'Lenght is', amount, unit

def processlenght(amount, inputunit, outputunit):
  lenght = Lenght(value=amount, unit=inputunit)
  
  if outputunit == 'mm':
    printlenght(amount=lenght.mm(), unit=outputunit)
  elif outputunit == 'cm':
    printlenght(amount=lenght.cm(), unit=outputunit)
  elif outputunit == 'm':
    printlenght(amount=lenght.m(), unit=outputunit)
  elif outputunit == 'km':
    printlenght(amount=lenght.km(), unit=outputunit)
  elif outputunit == 'inch':
    printlenght(amount=lenght.inch(), unit=outputunit)
  elif outputunit == 'foot':
    printlenght(amount=lenght.foot(), unit=outputunit) 
  elif outputunit == 'yard':
    printlenght(amount=lenght.yard(), unit=outputunit)
  elif outputunit == 'mile':
    printlenght(amount=lenght.mile(), unit=outputunit)
  else:
    print 'requested unit', outputunit, 'does not exist or is not supported'

