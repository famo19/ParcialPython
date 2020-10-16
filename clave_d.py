import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*3 = 24
"""


# start-->
def multiplicar(num1, num2, num3):
    return num1*num2*num3


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1000 al 2000
"""


# start-->
def sumaDivTresYCincoPlus():
    result = 0
    i=1000
    while i>=1000 and i<=2000:
        if i%3==0 and i%5==0:
            result+=i
            i+=1
        else:
            i+=1
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area y el volumen de un ortoedro
longitud = 10 m
latitud = 6 m
altura = 5 m

area: A = 2(longitud · latitud + longitud · altura + latitud · altura)
volumen: V = longitud · latitud · altura
"""


# start-->
def definicionOrtoedro(num1,num2,num3):
    result= dict(area=obtenerArea(num1,num2,num3), volumen=obtenerVolumen(num1,num2,num3))
    return result


def obtenerArea(num1,num2,num3):
    result=2*(num1*num2+num1*num3+num2*num3)
    return result


def obtenerVolumen(num1,num2,num3):
    result= num1*num2*num3
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Ortoedro:
    def __init__(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
    def definicionOrtoedro(self):
        result=dict(area=obtenerArea(self.num1, self.num2,self.num3), volumen=obtenerVolumen(self.num1, self.num2,self.num3))
        return result

    def obtenerArea(self):
        result=2*(self.num1*self.num2+self.num1*self.num3+self.num2*self.num3)
        return result

    def obtenerVolumen(self):
        result= self.num1*self.num2*self.num3
        return result
"""
***************************************************************
@@ ejercicio 5 @@
VentaComputadoras
Computadora
    procesador
    ram
    tarjeta_grafica
    ssd
    costo
    conDescuento
    descuento
    conPlazo
    cuota
"""


class VentaComputadoras:
    def __init__(self, Computadora):
        self.Computadora=list(Computadora())
        

    def orden(self):
        return self.Computadora

    def totalProcesadorIntel(self):
        for element in range(len(self.Computadora)):
            for element2 in range(Computadora()): 
        return 0

    def totalRam16ConDescuento(self):
        return 0


class Computadora:
    def __init__(self,procesador, ram, tarjeta_grafica, ssd, costo, conDescuento, descuento, conPlazo, cuota):
        self.procesador=procesador
        self.ram=ram
        self.tarjeta_grafica=tarjeta_grafica
        self.ssd=ssd
        self.costo=costo
        self.conDescuento=conDescuento
        self.descuento=descuento
        self.conPlazo=conPlazo
        self.cuota=cuota
    
    
    


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
