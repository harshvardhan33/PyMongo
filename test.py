# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 20:44:25 2020

@author: harshvardhan
"""

import numpy as np


u1 = np.array(np.random.rand(100))
u = np.random.rand(1000)

for i in range(len(u1)):
    z=np.sqrt(-2*np.log(u1[i]))