#!/usr/bin/python
#Filename: str_format.py

>>> '{0:.3}'.format(1/3) # decimal (.) precision of 3 for float
'0.333'
>>> '{0:_^11}'.format('hello') # fill with underscores (_) with the text centered (^) to 11 width
'___hello___'
>>> '{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python') # keyword-based
'Swaroop wrote A Byte of Python'
