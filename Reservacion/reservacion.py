import datetime
from datetime import timedelta
from decimal import Decimal

class ValidarEntrada:
    def validarFecha(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%d-%m-%Y')
        except ValueError:
                raise ValueError("Formato de fecha erroneo, deberia ser 'dd-mm-aaaa'")
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
    def validarTasa(self,tasa):
        if (tasa < 0):
            raise Exception("La tasa no puede ser negativa")
            
    
class Calculo:    
    def calculohoras (self, fchcomienzo, fchfinal):
        if fchcomienzo <= fchfinal:
            difference = fchfinal - fchcomienzo    
            return (difference.total_seconds()/60/60)
        else:
            return -1
    
    def calculomonto(self, tarif, fchcomienzo, fchfinal):
        recorrer = fchcomienzo
        
        tasaD = tarif.obtenerTasaDiurna()
        tasaN = tarif.obtenerTasaNocturna()
        
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
    def __init__(self, tasaDiurna = 0, tasaNocturna = 0):
        self.tasaDiurna = tasaDiurna
        self.tasaNocturna = tasaNocturna
    def definirTasaDiurna(self,tasa):
        self.tasaDiurna = tasa
    def definirTasaNocturna(self,tasa):
        self.tasaNocturna = tasa
    def obtenerTasaDiurna(self):
        return self.tasaDiurna
    def obtenerTasaNocturna(self):
        return self.tasaNocturna
    
class Entrada:
    def __init__(self, tasaDiurna = 0, tasaNocturna = 0, fechaInicial = "00-00-0000",
                  fechaFinal = "00-00-0000", horaInicial = "00:00", horaFinal = "00:00"):
        self.tasaDiurna = tasaDiurna
        self.tasaNocturna = tasaNocturna
        self.fechaInicial = fechaInicial
        self.fechaFinal = fechaFinal
        self.horaInicial = horaInicial
        self.horaFinal = horaFinal
    def definirTarifaDiurna(self,tarifa):
        self.tasaDiurna = tarifa
    def definirTarifaNocturna(self,tarifa):
        self.tasaNocturna = tarifa    
    def definirFechaInicio(self, fecha):
        self.fechaInicial = fecha
    def definirFechaFinal(self, fecha):
        self.fechaFinal = fecha
    def definirHoraInicio(self, hora):
        self.horaInicial = hora
    def definirHoraFinal(self, hora):
        self.horaFinal = hora
    
    def obtenerTarifaDiurna(self):
        return self.tasaDiurna
    def obtenerTarifaNocturna(self):
        return self.tasaNocturna    
    def obtenerFechaInicio(self):
        return self.fechaInicial
    def obtenerFechaFinal(self):
        return self.fechaFinal
    def obtenerHoraInicio(self):
        return self.horaInicial
    def obtenerHoraFinal(self):
        return self.horaFinal
    
    def main(self):
        """Entrada Manual
        #Ingreso de fechas, horas y tarifa
        tarifaDiurna = input("Ingresa la tarifa diurna: ")
        tarifaNocturna = input("Ingresa la tarifa nocturna: ")
            
        fechaComienzo = input("Ingresa la fecha de comienzo con el formato 'dd-mm-aaaa': ")
        horaComienzo = input("Ingresa la hora de comienzo con el formato militar '21:03': ")
        
        fechaFinalizacion = input("Ingresa la fecha de finalizacion con el formato 'dd-mm-aaaa': ")
        horaFinalizacion = input("Ingresa la hora de finalizacion con el formato militar '21:03': ")
        """
        
        """Verificar entradas"""
        ver = ValidarEntrada()
        ver.validarFecha(self.obtenerFechaInicio())
        ver.validarFecha(self.obtenerFechaFinal())
        ver.validarHora(self.obtenerHoraInicio())
        ver.validarHora(self.obtenerHoraFinal())
        ver.validarTasa(Decimal(self.obtenerTarifaDiurna()))
        ver.validarTasa(Decimal(self.obtenerTarifaNocturna()))
        
        """Se hace parsing y se convierte a numeros"""
        """Fechas"""
        fechaCFormat = self.obtenerFechaInicio().split('-')
        fechaFFormat = self.obtenerFechaFinal().split('-')
        diaC = int(fechaCFormat[0])
        mesC = int(fechaCFormat[1])
        anioC = int(fechaCFormat[2])
        diaF = int(fechaFFormat[0])
        mesF = int(fechaFFormat[1])
        anioF = int(fechaFFormat[2])
        """Dias"""
        horaCFormat = self.obtenerHoraInicio().split(':')
        horaFFormat = self.obtenerHoraFinal().split(':')
        horaC = int(horaCFormat[0])
        minutoC = int(horaCFormat[1])
        horaF = int(horaFFormat[0])
        minutoF = int(horaFFormat[1])
        
        """Tarifa"""
        tarif = Tarifa()
        tarif.definirTasaDiurna(Decimal(self.obtenerTarifaDiurna()))
        tarif.definirTasaNocturna(Decimal(self.obtenerTarifaNocturna()))
        
        """Se crean los tipos datetime"""
        t = datetime.time(horaC, minutoC, 0)
        d = datetime.date(anioC, mesC, diaC)
        fchcomienzo = datetime.datetime.combine(d, t)
        tf = datetime.time(horaF, minutoF,0)
        df = datetime.date(anioF, mesF, diaF)
        fchfinal = datetime.datetime.combine(df, tf)
        
        ver.validarTiempoReserva(fchcomienzo, fchfinal)
        x = Calculo()
        return x.calculomonto(tarif, fchcomienzo, fchfinal)
    
