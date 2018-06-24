
from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import math
from tensorflow.examples.tutorials.mnist import input_data
# 搜尋 need
    
def hdiv(dividend, divisor, precision=0):  
    """高精度计算除法，没有四舍五入 
     
    @author: cidplp 
     
    @param dividend:被除数 
    @type dividend:int 
    @param divisor:除数 
    @type divisor:int 
    @param precision:小数点后精度 
    @type precision:int 
    @return:除法结果 
    @rtype:str 
    """  
      
    if isinstance(precision, int) == False or precision < 0:  
        print('精度必须为非负整数')  
        return  
      
    a = dividend  
    b = divisor  
      
    #有负数的话做个标记  
    if abs(a+b) == abs(a) + abs(b):  
        flag = 1  
    else:  
        flag = -1      
      
    #变为正数，防止取模的时候有影响  
    a = abs(a)  
    b = abs(b)  
  
    quotient = a // b  
    remainder = a % b  
      
    if remainder == 0:  
        return quotient  
      
    ans = str(quotient) + '.'  
  
    i = 0  
    while i < precision:  
        a = remainder * 10  
        quotient = a // b  
        remainder = a % b   
        ans += str(quotient)  
        if remainder == 0:  
            break  
        i += 1  
      
    if precision == 0:  
        ans = ans.replace('.', '')  
      
    if flag == -1:  
        ans = '-' + ans  
      
    return ans

def fractionToDecimal(numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    sign = '-' if numerator * denominator < 0 else ''
    quotient, remainder = divmod(abs(numerator), abs(denominator))
    result_list = [sign, str(quotient), '.']
    remainders = []
    i=0
    while remainder not in remainders:
        remainders.append(remainder)
        quotient, remainder = divmod(remainder * 10, abs(denominator))
#         if(i%1000==0):
#             print(str(i))
        i = i+1
        result_list.append(str(quotient))
    
    print(str(i))
    idx = remainders.index(remainder)
    result_list.insert(idx + 3, '(')
    result_list.append(')')
    result = ''.join(result_list).replace('(0)', '').rstrip('.')
    return result


def validate_No2No5(num1_t, num2_t, result):
    print(str(num1_t[0])+'/'+str(num1_t[1])+'*'+str(num2_t[0])+'/'+str(num2_t[1]) +' = '+ str(num1_t[0]*num2_t[0]) + '/' + str(num1_t[1]*num2_t[1]))
    
    resultstr = str(result)
    len_answer = len (resultstr[resultstr.index('.')+2 : len(resultstr)-1] )
    len_predict = len(str(num1_t[1]))*len(str(num2_t[1]))
    validate = '正確' if len_answer%(len_predict)==0 else '錯誤'
    print('*** 循環長度: '+str(len_answer) +'  ###'+validate+' (\'正確\'的意思是有時 長度，可以分解為:  '+str(len_answer//(len_predict))+'* '+str(len_predict)+'='+str(len(str(num1_t[1])))+'*'+str(len(str(num2_t[1]))))
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(result)
# 分數的分母與分子，位數一樣。
def division_p(num1_t, num2_t):
    numerator = num1_t[0]*num2_t[0]
    denominator = num1_t[1]*num2_t[1]
    result = fractionToDecimal(numerator, denominator) #fractionToDecimal(70077626, 999890001)
    validate_No2No5(num1_t, num2_t, result) 
    return result

fp = open("filenameW.txt", "a")
result = division_p((1,1234567891011121314151617181920 ),(1, 1))
fp.write(result+'\n')
raise SystemExit(0)
fp = open("filename1.txt", "a")
fp.truncate()
for i in range(100):
    i = i+1
    result = division_p((i,9999),(i, 9999))
    fp.write(result+'\n')   
fp.close()
raise SystemExit(0)    
raise SystemExit(0)

#     xx = hdiv(1*1, 9999*9999, 100000)    fp.truncate()
 
# division_p((23456789,99999999),(1234567, 9999999)) 

# need to be corrected: 123/999 = 123123/999999 但是程式邏輯還沒考慮到這種情況
# division_p((2345678923456789,9999999999999999),(12345671234567, 99999999999999))        
raise SystemExit(0)    



bb=int('123', 10).to_bytes(8, 'big')
bb= '{0:b}'.format(int(xx[2:]))            

division_p((1,999),(1,999))
raise SystemExit(0)
print('End')
print(hdiv(3456789*123456, 9999999*999999, 2000))
print(hdiv(23456789*1234567, 99999999*9999999, 2000))
              
print(hdiv(6789*123, 9999*999, 100))
print(hdiv(56789*1234, 99999*9999, 400))
print(hdiv(456789*12345, 999999*99999, 2000))

print("-------------------------------------------")
print(1/13)
print(hdiv(1, 13, 50))
print(hdiv(142857, 999999, 50))



for i in range(102):
    res = hdiv(1, i+1, 100)
    print( '1/'+str(i+1)+': '+str(res)) 
    
raise SystemExit(0) 
 





# quotient = 7 // 3  
# remainder = 7 % 3
# print(quotient) 
# print(remainder)
A = np.array([1,1,1])
B = np.array([2,2,2])
print(A[np.newaxis, :])
print(A[np.newaxis,:].shape)
print(A[np.newaxis, :].T)
print(A[np.newaxis,:].T.shape)

print( A[:,np.newaxis])
print( A[:, np.newaxis].shape)
print( A[:,np.newaxis].T)
print( A[:, np.newaxis].T.shape)

print(A)
print(A.shape)
print(A.T)
print(A.T.shape)
D = np.vstack((A,B)) 
print(D)
print(D.shape)
x = np.arange(24).reshape(2,3,4)
print(x)
print(x.shape)
 











