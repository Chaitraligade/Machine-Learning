# -*- coding: utf-8 -*-
"""ML 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S6VeN4J76RPkBOQteM-dmuNvVAopenzp
"""

import matplotlib as plot
import numpy as np
import sympy as sym       #Lib for Symbolic Math
from matplotlib import pyplot

def objective(x):
  return (x+3)**2

def derivative(x):
  return 2*(x + 3)

def gradient_descent(alpha, start, max_iter):
  x_list = list()
  x= start;
  x_list.append(x)
  for i in range(max_iter):
    gradient = derivative(x);
    x = x - (alpha*gradient);
    x_list.append(x);
  return x_list

alpha = 0.1       #Step_size
start = 2         #Starting point
max_iter = 30     #Limit on iterations
x = sym.symbols('x')
expr = (x+3)**2;   #target function

x_cordinate = np.linspace(-15,15,100)
pyplot.plot(x_cordinate,objective(x_cordinate))
pyplot.plot(2,objective(2),'ro')

X = gradient_descent(alpha,start,max_iter)

x_cordinate = np.linspace(-5,5,100)
pyplot.plot(x_cordinate,objective(x_cordinate))

X_arr = np.array(X)
pyplot.plot(X_arr, objective(X_arr), '.-', color='red')
pyplot.show()