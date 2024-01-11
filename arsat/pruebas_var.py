# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:32:23 2024

@author: calanis
"""
#Think of a recursive version of the funtion f(n)=3*n
class f_1() :                                       #para obtener un resultado -> object(n)
    def __init__(self):
        self.aux = 3
    
    def __call__(self,k):
        if k == 1:
            return self.aux
        else:
            return self.__call__(k-1) + self.aux

class f_2() :                                       #son equivalentes solo que para obtener un resultado -> object.operation(n)
    def __init__(self):
        self.aux = 3
    
    def operation(self,k):
        if k == 1:
            return self.aux
        else:
            return self.operation(k-1) + self.aux

#Write a recursive Python function that returns the sum of the first n integers. (Hint: The function will be similiar to the factorial function!)



class f_3():
    def __init__(self):
        pass
    def __call__(self,k):
        if k == 1 :
            return 1
        else:
            return k + self.__call__(k-1)
        
# Write a function which implements the Pascal's triangle:


#           1

#         1   1

#       1   2   1

#     1   3   3   1

#   1   4   6   4   1

# 1   5   10   10   5   1


# resolucion sin recursion


























