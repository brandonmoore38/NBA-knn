# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 02:41:38 2016

@author: alsherman
"""
TypeError
NameError
IndentationError
SyntaxError

x
NameError: name 'x' is not defined


x = 5
if x == 5:
print x
IndentationError: expected an indented block


'2' + 2             
TypeError: cannot concatenate 'str' and 'int' objects


def get_distance(rate=10, time):
    return rate * time
SyntaxError: non-default argument follows default argument

x = "python
SyntaxError: EOL while scanning string literal