# -*- coding: utf-8 -*-
# 
# pip install --upgrade numpy
# pip install --upgrade plotVectors
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import sympy
import collections
from sympy import pprint

# 質因數分解   
dict_p = sympy.factorint(1234567891011121314151617181920, visual=True)
# dict_p = collections.OrderedDict(sorted(dict_p.items()))
print(type(dict_p))
pprint(dict_p)
raise SystemExit(0)
for i in range(1000000):
    print(i/123456789)


a_str = ("123","999")
b_str = ("12", "99")
a_mod = len(a_str[0])
b_mod = len(b_str[0])
a_list = [ int(digit) for digit in a_str[0] ]
b_list = [ int(digit) for digit in b_str[0] ]
col_seq = {}
for c in range(a_mod):
    idx_b = c
    idx_a = 1
    temp = []
    for mn in range(a_mod*b_mod):
        idx_b = 1 if idx_b >= b_mod else ++idx_b
        print(idx_b)    
        
# filename = 'default.properties' if len(sys.argv) == 1 else sys.argv[1]

a = np.array([])


raise SystemExit(0)  





