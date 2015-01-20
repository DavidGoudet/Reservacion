from reservacion import *
import unittest


class CasosDePruebaReservaciones(unittest.TestCase):
        
        def ejecutarReservacion(self, fchini, fchfinal, horaini, horafinal, tasaD, tasaN):
            entrada = Entrada()
            entrada.definirFechaInicio(fchini)
            entrada.definirFechaFinal(fchfinal)
            entrada.definirHoraInicio(horaini)
            entrada.definirHoraFinal(horafinal)
            entrada.definirTarifaDiurna(tasaD)
            entrada.definirTarifaNocturna(tasaN)       
            return entrada.main()
    
    
        def testFechaMinima(self):
            self.failUnless(100 == self.ejecutarReservacion("01-01-0001","01-01-0001","0:00","1:00","100.00","100.00"))
            
        def testFechaMaxima(self):
            self.failUnless(100 == self.ejecutarReservacion("31-12-9999","31-12-9999","23:00","23:59","100.00","100.00"))
            
        def testTasaMinima(self):
            self.failUnless(0 == self.ejecutarReservacion("31-12-9999","31-12-9999","23:00","23:59","0.00","0.00"))
        
        """maxint de Python 2, no hay maximo para Python 3"""
        def testTasaMaxima(self):
            self.failUnless(27670116110564327421 == self.ejecutarReservacion("31-12-9999","31-12-9999","21:00","23:59","9223372036854775807","9223372036854775807"))
            
        def testQuinceMinutos(self):
            self.failUnless(200 == self.ejecutarReservacion("01-01-0001","01-01-0001","5:50","6:05","100.00","200.00"))
        
        def testSetentaYDosHoras(self):
            self.failUnless(10800 == self.ejecutarReservacion("01-01-0001","04-01-0001","0:00","0:00","100.00","200.00"))
        
            
if __name__ == '__main__':
    unittest.main()    