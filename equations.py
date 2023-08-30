# -*- coding: utf-8 -*-
import sys
import numpy as np
sys.path.append(r"lib")
from  mathematics import second_derivative
#%%
def equation(x, a3, a2, a1, a0):
    """
    
    """
    
    y  = a3*x**3+a2*x**2+a1*x+a0
    yd2 = second_derivative(x, y)
    
    return y, yd2


import matplotlib.pyplot as plt
a3=0.5
a2=1
a1=2
a0=5
x  = np.linspace(0, 100 ,101)
y, yd2 = equation(x, a3, a2, a1, a0)
fig, ax = plt.subplots(1,2)
ax[0].plot(x, y)
ax[1].plot(x, yd2)