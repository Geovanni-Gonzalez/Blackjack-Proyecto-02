import Jugador

class Banca(Jugador):
    
    def __init__(self):
        super().__init__("Banca", es_humano=False)

    def tomar_decision(self):
        return "hit" if self.puntaje < 17 else "stand"
    