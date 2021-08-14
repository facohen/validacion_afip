# CUIT
import regex
class Cuit:

    def __init__(self, cuit):
        self.cuit = cuit

    def chequear_longitud(self):
        return len(self.cuit)

    def extraer_numeros(self):
        return re.sub('\D', '', self.cuit)

    def calcular_vercleaificador(self):
        multiplicador  = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        verificador = self.cuit[-1]  
        resultado = 0 

        i = 0
        for digito in self.cuit:
            resultado +=  multiplicador[i] * self.cuit[i+1]
            i += 1
            resultado = resultado % 11
            resultado = 11 - resultado

        if resultado == 11:
            resultado == 0
        elif resultado == 10:
            resultado = 9
    
        if resultado == verificador:
            return self.cuit
        return 0 
    
    def validar_cuit(self):
        self.extraer_numeros()
        if self.chequear_longitud() != 11:
            return 0
        return self.calcular_verificador()

        








