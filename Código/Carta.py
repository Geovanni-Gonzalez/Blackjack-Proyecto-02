class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
        self.valor_numerico = self.calcular_valor()

    def calcular_valor(self):
        if self.valor in ['J', 'Q', 'K']:
            return 10
        elif self.valor == 'A':
            return 11  # El valor del As puede ser ajustado en el cálculo de puntaje
        else:
            return int(self.valor)

    def obtener_valor(self):
        return self.valor_numerico
    
    