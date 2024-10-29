from flask import Flask, render_template, request, redirect, url_for, session
import random
import json
import Juego


app = Flask(__name__)

# Función para barajar y repartir cartas
def barajar_cartas():
    """Devuelve un mazo de cartas barajadas."""
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    mazo = [(valor, palo) for palo in palos for valor in valores]
    random.shuffle(mazo)
    return mazo


@app.route('/')
def inicio():
    """
    Muestra la página de inicio con las opciones de juego, reglas y perfil.
    """
    return render_template('index.html')

@app.route('/jugar')
def jugar():
    """
    Ruta para iniciar el juego. Muestra el tablero de juego.
    """
    # Inicializar el estado del juego, jugadores y banca.
    return render_template('juego.html')

# Ruta para la configuración del juego
@app.route('/configuracion', methods=['GET', 'POST'])
def configuracion():
    
    return render_template('configuracion.html')

# Ruta para iniciar el juego en modo Jugador vs Jugador
@app.route('/juego/jugador-vs-jugador')
def jugar_jugador_vs_jugador_post():
    return render_template('juego.html')





# Ruta para iniciar el juego en modo Jugador vs IA
@app.route('/juego/jugador-vs-ia')
def jugar_jugador_vs_ia():
    return render_template('juego_ia.html')



if __name__ == '__main__':
    app.run(debug=True)
