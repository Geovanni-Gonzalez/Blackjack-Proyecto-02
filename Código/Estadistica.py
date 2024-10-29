class Estadisticas:
    def __init__(self):
        self.partidas_jugadas = 0
        self.victorias = {}
        self.precision_decisiones = {}

    def actualizar_estadisticas(self, jugador, resultado):
        self.partidas_jugadas += 1
        if jugador.nombre not in self.victorias:
            self.victorias[jugador.nombre] = 0
        if resultado == "Ganó":
            self.victorias[jugador.nombre] += 1

    def mostrar_resumen(self):
        print(f"Partidas jugadas: {self.partidas_jugadas}")
        for jugador, victorias in self.victorias.items():
            print(f"{jugador}: {victorias} victorias")