import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 2 numeros
2*4 = 8
"""


# start-->
def multiplicar(numero1, numero2):
    return numero1*numero2


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1 al 1000
"""


# start-->
def sumaDivTresYCinco():
    result = 0
    total = 0

    while result < 1000:
        if (result%3 == 0) and (result%5 == 0):
            total = total + result
    
        result = result + 1

    return total


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el generatriz, area y el volumen de un cono
radio = 5 m
altura = 11 m
generatriz: square_root(altura^2 + radio^2)
area: pi*radio*(radio+generatriz)
volumen: (1/3)*pi*radio^2*altura
"""


# start-->

    
def obtenerGeneratriz():
    result = math.sqrt((11 ** 2) + (5 ** 2))
    return result

def obtenerArea():
    result = math.pi * 5 * (5 + obtenerGeneratriz())
    return result


def obtenerVolumen():
    result = (1 / 3) * math.pi * (5 ** 2) * 11
    return result


def definicionCono():
    generatriz = obtenerGeneratriz()
    area = obtenerArea()
    volumen = obtenerVolumen()
    result = {
        "generatriz": generatriz,
        "area": area,
        "volumen": volumen
    }
    

    
    return result

    #print(result)









"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase
"""


# start-->
class Cono:
    def definicionCono(self):
        return definicionCono()

    def obtenerGeneratriz(self):
        result = math.sqrt((11 ** 2) + (5 ** 2))
        return result

    def obtenerArea(self):
        result = math.pi * 5 * (5 + obtenerGeneratriz())
        return result


    def obtenerVolumen(self):
        result = (1 / 3) * math.pi * (5 ** 2) * 11
        return result


    def definicionCono(self):
        generatriz = obtenerGeneratriz()
        area = obtenerArea()
        volumen = obtenerVolumen()
        result = {
            "generatriz": generatriz,
            "area": area,
            "volumen": volumen
        }
        

        
        return result


"""
***************************************************************
@@ ejercicio 5 @@
CentroMedico
Paciente
    nombre
    lugar
    descripcion
    costo
    conDescuento
    descuento
"""


class CentroMedico:
    def registrar(self, nombre, lugar, descripcion, costo, conDescuento, descuento):
        self.pacientes = []

        self.pacientes.append(nombre, lugar, descripcion, costo, conDescuento, descuento)



    def totalCostoSanSalvador(self, nombre, lugar, descripcion, costo, conDescuento, descuento):
        
        total = 0
        for i in self.pacientes:
            if lugar == "San Salvador":
                total = total + costo
        
        return total


    def totalCostoConDescuento(self):
        return 0


class Paciente:
    def __init__(self, nombre, lugar, descripcion, costo, conDescuento, descuento):
        self.nombre = nombre
        self.lugar = lugar
        self.descripcion = descripcion
        self.costo = costo
        self.conDescuento = conDescuento
        self.descuento = descuento

    def getCostoTotal(self):
        return self.costo

    def getLugar(self):
        return self.lugar


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
    return "https://github.com/LuisGonzalez32/parcial.git"