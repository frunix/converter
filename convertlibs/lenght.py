from __future__ import division
__author__ = "Frederik Gowy"

class Lenght:
  """
  Lenght class, takes 2 arguments: a value and the unit.
  Value is an integer/floating point.
  Where unit is the one in which the value is given.
  Example: cm, inch, km, mile

  Methods to use:
  for each unit there will be a method with its name.
  Example: km is .km()
  See help() output for full details.
  """

  def __init__(self, value=0, unit='cm', rounding=2):
    self.__value = value
    self.__unit = unit
    self.__rounding = rounding

    # metrics system input
    if self.__unit == 'cm':
      self.__cm = self.__value
    elif self.__unit == 'mm':
      self.__cm = self.__mmTocm()
    elif self.__unit == 'm':
      self.__cm = self.__mTocm()
    elif self.__unit == 'km':
      self.__cm = self.__kmTocm()
    # Imperial system input
    elif self.__unit == 'inch':
      self.__cm = self.__inchTokm()
    elif self.__unit == 'foot' or self.__unit == 'feet':
      self.__cm = self.__footTocm()
    elif self.__unit == 'yard':
      self.__cm = self.__yardTocm()
    elif self.__unit == 'mile':
      self.__cm = self.__mileTocm()
    else:
      print 'unit given to lenght class not supported'
      print 'given unit:', self.__unit
      exit(1)

  # functions used in the init to convert from * to cm

  def __mmTocm(self):
    """
    converts self.__value from mm to cm and returns its value
    """

    expression = str(self.__value) + ' / 10'
    cm = eval(expression)
    return cm

  def __mTocm(self):
    
    expression = str(self.__value) + ' * 100'
    cm = eval(expression)
    return cm

  def __kmTocm(self):

    expression = str(self.__value) + ' * 100000'
    cm = eval(expression)
    return cm

  def __inchTocm(self):

    expression = str(self.__value) + ' * 2.54'
    cm = eval(expression)
    return cm

  def __footTocm(self):

    expression = str(self.__value) + ' * 30.48'
    cm = eval(expression)
    return cm

  def __yardTocm(self):

    expression = str(self.__value) + ' * 91.44'
    cm = eval(expression)
    return cm

  def __mileTocm(self):

    expression = str(self.__value) + ' * 160934'
    cm = eval(expression)
    return cm

  # external functions to calculate the requested unit.

  # Metric system units

  def cm(self):

    calculatedlenght = float(self.__cm)
    return round(calculatedlenght, self.__rounding)

  def mm(self):

    expression = str(self.__cm) + ' * 10'
    calculatedlenght = float(eval(expression))
    return round(calculatedlenght, self.__rounding)

  def m(self):

    expression = str(self.__cm) + ' * 0.1'
    calculatedlenght = float(eval(expression))
    return round(calculatedlenght, self.__rounding)

  def km(self):

    expression = str(self.__cm) + ' * 0.00001'
    calculatedlenght = float(eval(expression))
    return round(calculatedlenght, self.__rounding)

  # Imperial units

  def inch(self):

    expression = str(self.__cm) + ' * 0.393701'
    calculatedlenght = float(eval(expression))
    return round(calculatedlenght, self.__rounding)

  def foot(self):

    expression = str(self.__cm) + ' * 0.0328084'
    calculatedlenght = float(eval(expression))
    return round(calculatedlenght, self.__rounding)

  def yard(self):

    expression = str(self.__cm) + ' * 0.0109361'
    calculatedlenght = float(eval(expression))
    return round(calculatedlenght, self.__rounding)

  def mile(self):

    expression = str(self.__cm) + ' * 0.0000062137'
    calculatedlenght = float(eval(expression))
    return round(calculatedlenght, self.__rounding)
