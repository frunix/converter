# Converter

## What is it?

Converter is a command line program writen in python that helps you to convert
from one unit to another, of from one system to another.

This is my first script that I started as a test to teach myself.
This means, it will be full of imperfect code, and I'm aware of this.
There is a list of code improvements I'm planning to do.

Anyway,
I put it on github in the hope people will see it, and teach me what I'm doing
wrongly.
Please, help me to improve my coding style.


## how to use it

    % ./convert.py temperature 1 celsius to fahrenheit
    Temperature is 33.8 fahrenheit
    % ./convert.py temp 5 kalvin to rankine
    Temperature is 9.0 rankine
    % ./convert.py lenght 7 km to mile
    Lenght is 4.35 mile
    % ./convert.py lenght 2 yard to mm
    Lenght is 1828.8 mm

## libraries

I tried to write the classes in such a way it would be reusable.
An example for temperature class:
    >>> temp = Temperature(temperature=10, system='celsius' )
    >>> temp.kalvin()
    283.15 

## Next steps

Still to define
