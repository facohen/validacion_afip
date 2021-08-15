# CUIT
import re
class Cuit:

    def __init__(self, cuit):
        self.cuit = cuit

    def chequear_longitud(self):
        return len(self.cuit)

    def extraer_numeros(self):
        self.cuit = re.sub('\D', '', self.cuit)

    def calcular_verificador(self):
        resultado = 0
        digitos_validacion = '5432765432'
        suma_validador = 0
        for i in range(0,10):
            suma_validador += int(self.cuit[i]) * int(digitos_validacion[i])
        suma_validador = 11 - (suma_validador % 11)
        if suma_validador == 11:
            suma_validador = 0
        elif suma_validador == 10:
            suma_validador = 9
        if int(self.cuit[10]) == suma_validador:
            return True, self.cuit
        else:
            return False, self.cuit

    
    def validar_cuit(self):
        self.extraer_numeros()
        print("numero:",self.cuit)
        if self.chequear_longitud() != 11:
            return 0
        return self.calcular_verificador()


cuit = Cuit('20-208926688-4')
print(cuit.validar_cuit())








