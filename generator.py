
from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
import sympy
#     
# print(sympy.factorint(169491525423728813559322033898305084745762711864406779661 ))
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





