# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 22:51:57 2022

@author: 88696
"""

class a:
    b = None
    
    
    class c() :
        def d(self, e) :
            a.b = e
            
    f = c()

class t(a) :
    a = 1
    
g = a()
a.f.d(1)
print(a.b)