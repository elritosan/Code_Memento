# jugador.py
from Models.memento import ClassMemento

class ClassJugador:
    def __init__(self):
        self.vida = 100
        self.nivel = 1
        self.experiencia = 0

    def combatir(self):
        print("⚔️ El jugador ha luchado y ganado experiencia.")
        self.vida -= 10
        self.experiencia += 50
        if self.experiencia >= 100:
            self.nivel += 1
            self.experiencia = 0
            print("🎉 ¡Subiste de nivel!")

    def guardar_progreso(self):
        return ClassMemento(self.vida, self.nivel, self.experiencia)

    def cargar_progreso(self, memento):
        estado = memento.get_estado()
        self.vida = estado["vida"]
        self.nivel = estado["nivel"]
        self.experiencia = estado["experiencia"]

    def mostrar_estado(self):
        print(f"💾 Estado del jugador: Vida={self.vida}, Nivel={self.nivel}, Experiencia={self.experiencia}")