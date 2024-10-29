class Jugador:
    
    def __init__(self, nombre, es_humano=True):
        self.nombre = nombre
        self.es_humano = es_humano
        self.mano = []
        self.puntaje = 0

    def pedir_carta(self, mazo):
        carta = mazo.repartir_carta()
        if carta:
            self.mano.append(carta)
            self.calcular_puntaje()

    def plantarse(self):
        pass  # Esta acción se representa como "quedarse con la mano actual"

    def calcular_puntaje(self):
        total = 0
        ases = 0
        for carta in self.mano:
            total += carta.obtener_valor()
            if carta.valor == 'A':
                ases += 1
        # Ajusta el valor de los Ases si el total es mayor a 21
        while total > 21 and ases:
            total -= 10
            ases -= 1
        self.puntaje = total
