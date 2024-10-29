"""
Clase Carta
Representa una carta, para Blackjack.
"""    
class Carta:
    
    """
    Constructor de la clase Carta.
    """
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
        self.valor_numerico = self.calcular_valor()
        self.visible=False


    """
    Nombre: calcular_valor
    Descripción: Calcula el valor numérico de la carta.
    Retorna: El valor numérico de la carta.
    """
    def calcular_valor(self):
        if self.valor in ['J', 'Q', 'K']:
            return 10
        elif self.valor == 'A':
            return 11  # El valor del As puede ser ajustado en el cálculo de puntaje
        else:
            return int(self.valor)
    """
    Nombre: obtener_valor
    Descripción: Obtiene el valor numérico de la carta.
    Retorna: El valor numérico de la carta.
    """
    def obtener_valor(self):
        return self.valor_numerico
    
    """
    Nombre: obtener_palo
    Descripción: Obtiene el palo de la carta
    Retorna: El palo de la carta
    """
    def obtener_palo(self):
        return self.palo

    """
    Nombre: obtener_nombre
    Descripción: Obtiene el nombre de la carta
    """
    def mostrar(self):
        self.visible=True

    """
    Nombre: ocultar
    Descripción: Oculta la carta
    """
    def ocultar(self):
        self.visible=False
    
