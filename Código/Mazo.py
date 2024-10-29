import random
import Carta

"""
Representa un mazo de cartas para un juego de blackjack.
"""
class Mazo:
    def __init__(self):
        palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cartas = [Carta(palo, valor) for palo in palos for valor in valores]
        self.barajar()

    def barajar(self):
        random.shuffle(self.cartas)

    def repartir_carta(self):
        return self.cartas.pop() if self.cartas else None
    
    def __len__(self):
        return len(self.cartas)
    
