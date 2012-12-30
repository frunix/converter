
__author__ = "Frederik Gowy"

class Temperature:
  """
  Temperature Class, takes 2 arguments: the temperature as a value and the 
  system.
  Temperature is an integer/floating point,
  where system is the name of in which the temperature is given.
  Example: celsius or kaling.

  Methods to use:
  the name of the system you want the temperature converted to.
  That is, .celsius() for output in celsius, .kalvin() for kalvin.

  By default, the results are rounded to 2 digits,
  this can be overwritten by adding an argument rounding with an integer.


  TODO
  ____
  Add support for Romer, Newton, Delisle, Reaumur
  """


  def __init__(self, temperature=0, system='c', rounding=2):
    self.__temperature = temperature
    self.__system = system
    self.__rounding = int(round(rounding))

    if self.__system == 'celsius':
      self.__celsius = self.__temperature
    elif self.__system == 'fahrenheit':
      self.__celsius = self.__fahrenheitToCelsius()
    elif self.__system == 'kalvin':
      self.__celsius = self.__kalvinToCelsius()
    elif self.__system == 'rankine':
      self.__celsius = self.__rankineToCelsius()
    else:
      print 'nonsupported system:', self.__system
      exit(1)

  # Functious used in the init to convert from * to celsius

  def __fahrenheitToCelsius(self):
    """
    converts self.__temperature from fahrenheit to celsius
    and returns its vallue
    """
    
    expression = '(' + str(self.__temperature) + ' - 32) * 0.5555555555556'       
    calculatedtemp = eval(expression)                                           
    return calculatedtemp
  
  def __kalvinToCelsius(self):
    """
    converts self.__temperature from kalvin to celsius
    end returns its value
    """

    expression = str(self.__temperature) + ' - 273.15'
    calculatedtemp = float(eval(expression))
    return calculatedtemp

  def __rankineToCelsius(self):
    """
    converts self.__temperature from Rankine to celsius
    end returns its value
    """

    expression = '(' + str(self.__temperature) + ' - 491.67) * 0.5555555555556'
    calculatedtemp = float(eval(expression))
    return calculatedtemp





  # Methods that are callable from outside to output the value in their
  # representative system
  # Example: .fahrenheit() will return the value in fahrenheit

  def celsius(self):
    """just returns self.__celsius rounded on 2 digits"""
    calculatedtemp = float(self.__celsius)
    return round(calculatedtemp, self.__rounding)

  def fahrenheit(self):
    """
    Takes no arguments,
    converts the previously calculated self.__celsius to fahrenheit 
    and returns the value rounded by the amount of digits defined in
    self.__rounding
    """

    expression = '(' + str(self.__celsius) + ' * 1.8) + 32 '
    calculatedtemp = float(eval(expression))
    return round(calculatedtemp, self.__rounding) 

  def kalvin(self):
    """
    Takes no arguments,
    converts the previously calculated self.__celsius to kalvin
    and returns the value rounded by the amount of digits defined in
    self.__rounding
    """

    expression = str(self.__celsius) + ' + 273.15'
    calculatedtemp = float(eval(expression))
    return round(calculatedtemp, self.__rounding) 

  def rankine(self):
    """
    Takes no arguments,
    converts the previously calculated self.__celsius to Rankine
    and returns the value rounded by the amount of digits defined in
    self.__rounding
    """

    expression = '(' + str(self.__celsius) + ' + 273.15) * 1.8'
    calculatedtemp = float(eval(expression))
    return round(calculatedtemp, self.__rounding) 

