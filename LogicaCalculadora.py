'''
Created on 14 mar. 2024

@author: laura

'''
class Calculadora:
    
    def __init__(self):
        self.primerNumero = 0
        self.operacion = ""
        self.segundoNumero = 0
        
    def sumar(self):
        return self.primerNumero + self.segundoNumero
    
    def restar(self):
        return self.primerNumero - self.segundoNumero
    
    def multiplicar(self):
        return self.primerNumero * self.segundoNumero
    
    def dividir(self):
        if self.segundoNumero == 0:
            return 
        else:
            return self.primerNumero / self.segundoNumero
    
    def realizarOperacion(self):
        if self.operacion == "+":
            return self.sumar()
        elif self.operacion == "-":
            return self.restar()
        elif self.operacion == "*":
            return self.multiplicar()
        elif self.operacion == "/":
            return self.dividir()
        else:
            return 
        
    def indicarOperacion_Numero(self, num, op):
        self.primerNumero = float(num)
        self.operacion = op
        
    def indicarSegundoNumero(self, num):
        self.segundoNumero = float(num)
