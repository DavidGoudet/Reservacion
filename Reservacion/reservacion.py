import datetime

class ValidarEntrada:
    def validarFecha(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%d-%m-%Y')
        except ValueError:
                raise ValueError("Formato de fecha erroneo, deberia ser 'dd-mm-aaa'")
    def validarHora(self, hour_text):
        try:
            datetime.datetime.strptime(hour_text, '%H:%M')
        except ValueError:
                raise ValueError("Formato de hora erroneo, deberia ser formato militar '21:03'")
            
    
class Calculo:    
    def calculohoras (self, fchcomienzo, fchfinal, horaFinal, minutoFinal):
        if fchcomienzo < fchfinal:
            difference = fchfinal - fchcomienzo
            print(difference.total_seconds()/60/60)
    def calculomonto(self,totalHoras,horaFinal, minutoFinal):
        if (horaFinal >= 18 and minutoFinal >= 1):
            pass
        
class Tarifa:
    __tasaDiurna = 0
    __tasaNocturna = 0
    def definirTasaDiurna(self,tasa):
        self.__tasaDiurna = tasa
    def definirTasaNocturna(self,tasa):
        self.__tasaNocturna = tasa
    def obtenerTasaDiurna(self):
        return self.__tasaDiurna
    def obtenerTasaNocturna(self):
        return self.__tasaNocturna
        
"""Main"""
"""Ingreso de fechas y horas"""
fechaComienzo = input("Ingresa la fecha de comienzo con el formato 'dd-mm-aaa': ")
horaComienzo = input("Ingresa la hora de comienzo con el formato militar '21:03': ")

fechaFinalizacion = input("Ingresa la fecha de finalizacion con el formato 'dd-mm-aaa': ")
horaFinalizacion = input("Ingresa la hora de finalizacion con el formato militar '21:03': ")

"""Verificar entradas"""
ver = ValidarEntrada()
ver.validarFecha(fechaComienzo)
ver.validarFecha(fechaFinalizacion)
ver.validarHora(horaComienzo)
ver.validarHora(horaFinalizacion)

"""Se hace parsing y se convierte a numeros"""
"""Fechas"""
fechaCFormat = fechaComienzo.split('-')
fechaFFormat = fechaFinalizacion.split('-')
diaC = int(fechaCFormat[0])
mesC = int(fechaCFormat[1])
anioC = int(fechaCFormat[2])
diaF = int(fechaFFormat[0])
mesF = int(fechaFFormat[1])
anioF = int(fechaFFormat[2])
"""Dias"""
horaCFormat = horaComienzo.split(':')
horaFFormat = horaFinalizacion.split(':')
horaC = int(horaCFormat[0])
minutoC = int(horaCFormat[1])
horaF = int(horaFFormat[0])
minutoF = int(horaFFormat[1])

"""Se crean los tipos datetime"""
t = datetime.time(horaC, minutoC, 0)
d = datetime.date(anioC, mesC, diaC)
fchcomienzo = datetime.datetime.combine(d, t)
tf = datetime.time(horaF, minutoF,0)
df = datetime.date(anioF, mesF, diaF)
fchfinal = datetime.datetime.combine(df, tf)
x = Calculo()
x.calculohoras(fchcomienzo, fchfinal, horaF, minutoF)