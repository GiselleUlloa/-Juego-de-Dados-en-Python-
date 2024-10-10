import random

def lanzar_dado():
    return random.randint(1, 6)

def comparar_resultados(player1_value, player2_value):
    if player1_value > player2_value:
        return "Jugador 1 gana"
    elif player2_value > player1_value:
        return "Jugador 2 gana"
    else:
        return "Empate"

def main():
    player1_score = 0
    player2_score = 0

    for i in range(10):
        print(f"\nRonda {i + 1}:")
        print("Turno del Jugador 1:")
        input("Presiona enter para lanzar el dado...")
        player1_value = lanzar_dado()
        print("Jugador 1 lanzó: ", player1_value)

        print("Turno del Jugador 2:")
        input("Presiona enter para lanzar el dado...")
        player2_value = lanzar_dado()
        print("Jugador 2 lanzó: ", player2_value)

        resultado = comparar_resultados(player1_value, player2_value)
        print(resultado)
        if resultado == "Jugador 1 gana":
            player1_score += 1
        elif resultado == "Jugador 2 gana":
            player2_score += 1

        input("Presiona enter para continuar a la siguiente ronda...")

    print("\n### Fin del juego ###")
    print("Puntuación final:")
    print("Jugador 1:", player1_score)
    print("Jugador 2:", player2_score)

    if player1_score > player2_score:
        print("¡Jugador 1 es el ganador del juego!")
    elif player2_score > player1_score:
        print("¡Jugador 2 es el ganador del juego!")
    else:
        print("¡El juego terminó en empate!")

if __name__ == '__main__':
    main()
