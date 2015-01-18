import datetime
from datetime import timedelta

class ValidarEntrada:
    def validarFecha(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%d-%m-%Y')
        except ValueError:
                raise ValueError("Formato de fecha erroneo, deberia ser 'dd-mm-aaa'")
    def validarTiempoReserva(self, fechacom, fechafinal):        
        tiempo = Calculo()
        horas = (0.25 <= tiempo.calculohoras(fechacom, fechafinal) <= 72)
        if (not horas):
            raise Exception("La reservacion debe estar entre 15 minutos y 72 horas")
        
    def validarHora(self, hour_text):
        try:
            datetime.datetime.strptime(hour_text, '%H:%M')
        except ValueError:
                raise ValueError("Formato de hora erroneo, deberia ser formato militar '21:03'")
            
    
class Calculo:    
    def calculohoras (self, fchcomienzo, fchfinal):
        if fchcomienzo <= fchfinal:
            difference = fchfinal - fchcomienzo    
            return (difference.total_seconds()/60/60)
        else:
            return -1
    
    def calculomonto(self, fchcomienzo, fchfinal):
        recorrer = fchcomienzo
        tasa = Tarifa()
        tasaD = tasa.obtenerTasaDiurna()
        tasaN = tasa.obtenerTasaNocturna()
        monto = 0
        while (recorrer < fchfinal):
            """Caso diurno"""
            if (6 <= recorrer.hour <= 16 or (recorrer.hour == 17 and recorrer.minute == 0)):
                
                monto = monto + tasaD
                
                """Caso cruzado"""
            elif (recorrer.hour == 17 and recorrer.minute > 0 or(recorrer.hour == 18 and recorrer.minute == 0)
                  or (recorrer.hour == 5 and recorrer.minute > 0) or(recorrer.hour == 6 and recorrer.minute == 0)):
                 
                if (tasaD >= tasaN):
                    monto = monto + tasaD
                else:
                    monto = monto + tasaN
                    
                """Caso nocturno"""
            elif (18 <= recorrer.hour or recorrer.hour <= 6):
                monto = monto + tasaN
                
            
            recorrer = recorrer + timedelta(hours=1)
        return monto
            
        
class Tarifa:
    def __init__(self):
        self.tasaDiurna = 0
        self.tasaNocturna = 0
    def definirTasaDiurna(self,tasa):
        self.tasaDiurna = tasa
    def definirTasaNocturna(self,tasa):
        self.tasaNocturna = tasa
    def obtenerTasaDiurna(self):
        return self.tasaDiurna
    def obtenerTasaNocturna(self):
        return self.tasaNocturna
        
"""Main"""
"""Ingreso de fechas, horas y tarifa"""
tarifaDiurna = input("Ingresa la tarifa diurna: ")
tarifaNocturna = input("Ingresa la tarifa nocturna: ")

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

"""Tarifa"""
tarif = Tarifa()
tarifD = tarif.definirTasaDiurna(int(tarifaDiurna))
tarifN = tarif.definirTasaDiurna(int(tarifaNocturna))

"""Se crean los tipos datetime"""
t = datetime.time(horaC, minutoC, 0)
d = datetime.date(anioC, mesC, diaC)
fchcomienzo = datetime.datetime.combine(d, t)
tf = datetime.time(horaF, minutoF,0)
df = datetime.date(anioF, mesF, diaF)
fchfinal = datetime.datetime.combine(df, tf)

ver.validarTiempoReserva(fchcomienzo, fchfinal)
x = Calculo()
print("El monto es:", x.calculomonto(fchcomienzo, fchfinal))