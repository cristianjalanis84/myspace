# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 13:30:02 2022

@author: calanis
"""

class Droid:
    def __init__(self, name):
        self.nombre = name
    
    def switch_on(self):                            #self:primer parametro , que hace ref a la instancia actual del objeto
        print("Hi! I'm a Driod. Can I help you?")
    
    def switch_off(self):
        print("Bye! I'm going to sleep")
        
        
k2so  = Droid('bb8') #k2so es una instancia del objeto Droid




class mobilePhone:
    
    
    def __init__(self,manufacture,screen_size,num_cores):
        self.manufacture=manufacture
        self.screen_size=screen_size
        self.num_cores=num_cores
        self.apps=[]
        self.staus=0
        
    def power_on(self):
        self.status=1
    
    def power_off(self):
        self.status=0
    
    
    def install_app(self,*app):
        l=len(app)
        for ii in range(l):
            self.apps.append(app[ii])
        
    
mymobile = mobilePhone('Samsung', 6.1, 8)   


class Fraction:
    def __init__(self,num,den):
        
        self.numerador = num/self.gcd(num,den)
        self.denominador = den/self.gcd(num,den)
        print(self.numerador)
        print('__')
        print(self.denominador)
    
    @staticmethod
    def gcd(a,b):
       
       if abs(a) > abs(b) :
           auxa = abs(a)
           auxb = abs(b)
       else :
           auxa = abs(b)
           auxb = abs(a)
       
       while auxb > 0:
          
           aux = auxb
           auxb = auxa - auxb *(auxa // auxb)
           auxa = aux
           
       return aux
   
    def __str__(self):
        
        print(self.numerador)
        print('__')
        print(self.denominador)
    
    def __add__(self,other_Fraction):
        auxa2 = other_Fraction.numerador/self.gcd(other_Fraction.numerador,other_Fraction.denominador)
        auxb2 = other_Fraction.denominador/self.gcd(other_Fraction.numerador,other_Fraction.denominador)
        
        auxden = self.denominador * auxb2
        auxnum = self.numerador * auxb2 + self.denominador * auxa2
        
        return Fraction(auxnum/self.gcd(auxnum,auxden),auxden/self.gcd(auxnum,auxden))
    
    def __sub__(self,other_Fraction):
        auxa2 = other_Fraction.numerador/self.gcd(other_Fraction.numerador,other_Fraction.denominador)
        auxb2 = other_Fraction.denominador/self.gcd(other_Fraction.numerador,other_Fraction.denominador)
        
        auxden = self.denominador * auxb2
        auxnum = self.numerador * auxb2 - self.denominador * auxa2
        
        return Fraction(auxnum/self.gcd(auxnum,auxden),auxden/self.gcd(auxnum,auxden))
    
    def __mul__(self,other_Fraction):
        auxa2 = other_Fraction.numerador/self.gcd(other_Fraction.numerador,other_Fraction.denominador)
        auxb2 = other_Fraction.denominador/self.gcd(other_Fraction.numerador,other_Fraction.denominador)
        
        auxnum = self.numerador * auxa2
        auxden = self.denominador * auxb2
        
        return Fraction(auxnum/self.gcd(auxnum,auxden),auxden/self.gcd(auxnum,auxden))
    
    
    
        
        
          
           
           
                     
               
               
               