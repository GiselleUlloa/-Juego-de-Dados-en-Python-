import unittest
from dados import lanzar_dado, comparar_resultados

class TestJuegoDeDados(unittest.TestCase):

    def test_inicializacion_puntajes(self):
        player1_score = 0
        player2_score = 0
        self.assertEqual(player1_score, 0, "Puntuación inicial de Jugador 1 no es 0")
        self.assertEqual(player2_score, 0, "Puntuación inicial de Jugador 2 no es 0")

    def test_numeros_aleatorios(self):
        for _ in range(1000):
            numero = lanzar_dado()
            self.assertTrue(1 <= numero <= 6, f"Número fuera de rango: {numero}")

    def test_comparacion_resultados(self):
        self.assertEqual(comparar_resultados(6, 3), "Jugador 1 gana")
        self.assertEqual(comparar_resultados(3, 6), "Jugador 2 gana")
        self.assertEqual(comparar_resultados(3, 3), "Empate")

    
    def test_acumulacion_puntajes(self):
        player1_score = 0
        player2_score = 0
        resultado = comparar_resultados(6, 3)
        if resultado == "Jugador 1 gana":
            player1_score += 1
        elif resultado == "Jugador 2 gana":
            player2_score += 1
        self.assertEqual(player1_score, 1)
        self.assertEqual(player2_score, 0)

        resultado = comparar_resultados(3, 6)
        if resultado == "Jugador 1 gana":
            player1_score += 1
        elif resultado == "Jugador 2 gana":
            player2_score += 1
        self.assertEqual(player1_score, 1)
        self.assertEqual(player2_score, 1)

if __name__ == '__main__':
    unittest.main()
