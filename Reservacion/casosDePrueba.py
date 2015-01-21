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
            self.assertTrue(100 == self.ejecutarReservacion("01-01-0001","01-01-0001","0:00","1:00","100.00","100.00"))
            
        def testFechaMaxima(self):
            self.assertTrue(100 == self.ejecutarReservacion("31-12-9999","31-12-9999","23:00","23:59","100.00","100.00"))
            
        def testTasaMinima(self):
            self.assertTrue(0 == self.ejecutarReservacion("31-12-9999","31-12-9999","23:00","23:59","0.00","0.00"))
        
        """maxint de Python 2, no hay maximo para Python 3"""
        def testTasaMaxima(self):
            self.assertTrue(27670116110564327421 == self.ejecutarReservacion("31-12-9999","31-12-9999","21:00","23:59","9223372036854775807","9223372036854775807"))
            
        def testQuinceMinutos(self):
            self.assertTrue(200 == self.ejecutarReservacion("01-01-0001","01-01-0001","5:50","6:05","100.00","200.00"))
        
        def testSetentaYDosHoras(self):
            self.assertTrue(10800 == self.ejecutarReservacion("01-01-0001","04-01-0001","0:00","0:00","100.00","200.00"))
        
        def testBordeHorarioDiurno(self):
            self.assertTrue(100 == self.ejecutarReservacion("01-01-0001","01-01-0001","17:44","17:59","100.00","200.00"))
            
        def testBordeHorarioNocturno(self):
            self.assertTrue(100 == self.ejecutarReservacion("01-01-0001","01-01-0001","17:44","17:59","100.00","200.00"))
            
        """Fallas"""
        def testTasaNegativa(self):
            self.assertRaises(Exception, self.ejecutarReservacion,"01-01-0001","04-01-0001","0:00","0:00","-100.00","200.00")
            
        def testFechaMenorQueMinima(self):
            self.assertRaises(Exception, self.ejecutarReservacion,"00-01-0001","04-01-0001","0:00","1:00","100.00","200.00")
        
        def testFechaMayorQueMaxima(self):
            self.assertRaises(Exception, self.ejecutarReservacion,"01-01-10000","01-01-10000","0:00","1:00","100.00","200.00")
            
        def testMasDeSetentaYDosHoras(self):
            self.assertRaises(Exception, self.ejecutarReservacion,"01-01-0001","05-01-0001","1:00","2:00","100.00","200.00")
            
        def testMenosDeQuinceMinutos(self):
            self.assertRaises(Exception, self.ejecutarReservacion,"01-01-0001","01-01-0001","1:00","1:02","100.00","200.00")
            
        def testFormatoFechaIncorrecto1(self):
            self.assertRaises(Exception, self.ejecutarReservacion,"1-1-999","01-01-9999","0:00","1:00","100.00","200.00")
        
        def testFormatoFechaIncorrecto2(self):
            self.assertRaises(Exception, self.ejecutarReservacion,"01-01-9999","1-19999","0:00","1:00","100.00","200.00")
            
        def testFormatoHoraIncorrecto1(self):
            self.assertRaises(Exception, self.ejecutarReservacion,"01-01-0001","04-01-0001","00","1:00","100.00","200.00")
            
        def testFormatoHoraIncorrecto2(self):
            self.assertRaises(Exception, self.ejecutarReservacion,"01-01-0001","04-01-0001","1:00","100","100.00","200.00")
            
       
if __name__ == '__main__':
    unittest.main()    