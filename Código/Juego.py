import Mazo
import Jugador
import JugadorIA

class Juego:
    def __init__(self, modoDeJuego):
        self.mazo = Mazo()
        self.modoDeJuego = modoDeJuego
        if self.modoDeJuego == "JugadorVsIA":
            self.jugadores = [Jugador("Jugador"), JugadorIA("IA")]
        elif self.modoDeJuego == "JugadorVsJugador":
            self.jugadores = [Jugador("Jugador 1"), Jugador("Jugador 2")]

        self.banca = Jugador("Banca", es_humano=False)

    def iniciar_juego(self):
        while True:
            self.jugar_ronda()



    def jugar_ronda(self):
        for jugador in self.jugadores:
            while jugador.puntaje < 21:
                pass

                


        # Turno de la banca
        while self.banca.puntaje < 17:
            self.banca.pedir_carta(self.mazo)

    def evaluar_resultados(self):
        resultados = {}
        for jugador in self.jugadores:
            if jugador.puntaje > 21:
                resultados[jugador.nombre] = "Perdió"
            elif self.banca.puntaje > 21 or jugador.puntaje > self.banca.puntaje:
                resultados[jugador.nombre] = "Ganó"
            elif jugador.puntaje < self.banca.puntaje:
                resultados[jugador.nombre] = "Perdió"
            else:
                resultados[jugador.nombre] = "Empate"
        return resultados

    def reiniciar(self):
        self.mazo = Mazo()
        for jugador in self.jugadores + [self.banca]:
            jugador.mano = []
            jugador.puntaje = 0