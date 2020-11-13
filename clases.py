from datetime import date
from datetime import datetime

class Consulta():
    def __init__(self, consulta, estado, dia, mes, anio):
        self.consulta = consulta
        self.estado = estado
        self.dia = dia
        self.mes = mes
        self.anio = anio
    
    def set_estado(self, estado):
        self.estado = estado
        
    def get_estado(self):
        return self.estado
        
    def deboReportarme(self):
        #import pdb; pdb.set_trace()
        today = date.today()
        if (diasHastaFecha(self.dia, self.mes, self.anio, today.day, today.month, today.year) > 15) and (self.estado == "pendiente"):
            return True
        else:
            return False

class Documento():
    def __init__(self, tipo, numero):
        self.tipo = tipo
        self.numero = numero
    def __str__(self):
        return str(self.tipo)+ " " + str(self.numero)
    def get_doc(self):
        return str(self.tipo)+ " " + str(self.numero)
        
    
class Persona():
    def __init__(self, nombre = None, apellido=None, fechaNac=None, edad=None, genero=None, ocupacion=None, ingresos=None):
        self.nombre = nombre
        self.apellido = apellido
        self.doc = []
        self.fechaNac = fechaNac
        self.edad = int(edad)
        self.genero = genero
        self.ocupacion = ocupacion
        self.ingresos = round((float(ingresos)), 2)
        self.consultasRealizadas = []
        
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.nombre
    
    def set_apellido(self, apellido):
        self.apellido = apellido
        
    def get_apellido(self):
        return self.apellido
        
    def add_doc(self,doc):
        self.doc.append(doc)
    
    def get_all_docs(self):
        aux = ""
        for doc in self.doc:
            aux += doc.get_doc() + " ; "
        return aux
        
    def set_fechaNac(self, fechaNac):
        self.fechaNac = fechaNac
    
    def get_fechaNac(self):
        return self.fechaNac
        
    def set_edad(self, edad):
        self.edad = int(edad)
    
    def get_edad(self):
        return self.edad
        
    def set_genero(self, genero):
        self.genero = genero
    
    def get_genero(self):
        return self.genero
        
    def set_ocupacion(self, ocupacion):
        self.ocupacion = ocupacion
    
    def get_ocupacion(self):
        return self.ocupacion
        
    def set_ingresos(self, ingresos):
        self.ingresos = round((float(ingresos)), 2)
    
    def get_ingresos(self):
        return self.ingresos

    def calcular_adulto_equivalente(self):
        """
        hasta9 contiene  en el indice 0 el valor para menores
        de un año, en el indice 1 el valor para un año, y así
        sucesivamente. desde10F contiene los valores para mujeres
        en listas en las que en el indice cero se almacena a qué
        edad corresponde (y en caso de tratarse de un rango, el
        valor más alto del rango), y en el indice 1 el valor
        de adulto equivalente. Lo mismo con desde10M para varones.
        """
        hasta9 = [0.35, 0.37, 0.46, 0.51, 0.55, 0.60, 0.64, 0.66, 0.68, 0.69]
        desde10F = [[10, 0.70],[11, 0.72], [12, 0.74], [14, 0.76], [17, 0.77], [29, 0.76], [45, 0.77], [60, 0.76], [75, 0.67], [200,0.63]]
        desde10M = [[10, 0.79],[11, 0.82], [12, 0.85], [13, 0.90], [14, 0.96], [15, 1], [16, 1.03], [17, 1.04], [29, 1.02], [60, 1.00], [75, 0.83], [200,0.74]]
        #De o a 9 comparación directa, de 10 en adelante comparación por género; si es mayor a la edad a la que apunta el índice, avanzo el indice
        if self.edad <=9:
            equiv = hasta9[self.edad]
            return equiv
        elif self.genero == "F":
            i=0
            while (self.edad > desde10F[i][0]):
                i+=1
            return desde10F[i][1]
        elif self.genero == "M":
            i=0
            while (self.edad > desde10M[i][0]):
                i+=1
            return desde10M[i][1]
            
    def describir(self):
        return (self.apellido + ", " + self.nombre + " " + self.get_all_docs() + " Fecha de nacimiento: " + str(self.fechaNac) + " Edad: " + str(self.edad) + " Género " + self.genero + " Ocupación: " + self.ocupacion + " Ingresos: " + str(self.ingresos))
        
class Consultante(Persona):
    def __init__(self, idConsultante, nombre = None, apellido=None, fechaNac=None, edad=None, genero=None, ocupacion=None, ingresos=None):
        Persona.__init__(self, nombre, apellido, fechaNac, edad, genero, ocupacion, ingresos)
        self.idConsultante = idConsultante
    def consultar(self, consulta, estado, dia, mes, anio):
        self.consultasRealizadas.append(Consulta(consulta, estado, dia, mes, anio))
    def describir(self):
        return ("El consultante N° " + str(self.idConsultante) + " tiene por datos: " + self.apellido + ", " + self.nombre + " " + self.get_all_docs() + " Fecha de nacimiento: " + str(self.fechaNac) + " Edad: " + str(self.edad) + " Género " + self.genero + " Ocupación: " + self.ocupacion + " Ingresos: " + str(self.ingresos))
    def hacerConsulta(self, consulta, estado, dia, mes, anio):
        self.consultasRealizadas.append(Consulta(consulta, estado, dia, mes, anio))
        
       

def diasHastaFecha(day1, month1, year1, day2, month2, year2): #expresar primera fecha desde, segunda hasta. Los meses en numeros del 1 al 12 sin anteponer 0
    """
    Funcion que calcula cuantos dias hay entre la primer y segunda fecha introducida tomada de la pagina: http://exponentis.es/programa-en-python-para-calcular-el-numero-de-dias-entre-dos-fechas
    """
    
    # Función para calcular si un año es bisiesto o no
    
    def esBisiesto(year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    
    # Caso de años diferentes
    
    if (year1<year2):
        
        # Días restante primer año
        
        if esBisiesto(year1) == False:
            diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
     
        restoMes = diasMes[month1] - day1
    
        restoYear = 0
        i = month1 + 1
    
        while i <= 12:
            restoYear = restoYear + diasMes[i]
            i = i + 1
    
        primerYear = restoMes + restoYear
    
        # Suma de días de los años que hay en medio
    
        sumYear = year1 + 1
        totalDias = 0
    
        while (sumYear<year2):
            if esBisiesto(sumYear) == False:
                totalDias = totalDias + 365
                sumYear = sumYear + 1
            else:
                totalDias = totalDias + 366
                sumYear = sumYear + 1
    
        # Dias año actual
    
        if esBisiesto(year2) == False:
            diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
        llevaYear = 0
        lastYear = 0
        i = 1
    
        while i < month2:
            llevaYear = llevaYear + diasMes[i]
            i = i + 1
    
        lastYear = day2 + llevaYear
    
        return totalDias + primerYear + lastYear
    
    # Si estamos en el mismo año
    
    else:
        
        if esBisiesto(year1) == False:
            diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
        llevaYear = 0
        total = 0
        i = month1
        
        if i < month2:
            while i < month2:
                llevaYear = llevaYear + diasMes[i]
                i = i + 1
            total = day2 + llevaYear - 1
            return total 
        else:
            total = day2 - day1
            return total

print("No debería haber 15: ",diasHastaFecha(2, 11, 2020, 11, 11, 2020))
print("Debería haber +15: ",diasHastaFecha(19, 3, 2020, 11, 11, 2020))
alguien = Consultante(1, "Gladys", "Schein", "20/10/80", 40 , "femenino", "desocupada", 8000)
print(alguien.describir())
alguien.hacerConsulta("Quiero saber cómo tener un abogado gratuito por cuota alimentaria", "pendiente", 12, 3, 2020)
print(alguien.consultasRealizadas[0].deboReportarme())