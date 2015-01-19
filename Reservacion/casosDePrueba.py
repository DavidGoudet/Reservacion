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
    
        def test(self):
            self.failUnless(100 == self.ejecutarReservacion("10-10-2012","10-10-2012","3:30","4:30","100","100"))
            
if __name__ == '__main__':
    unittest.main()    