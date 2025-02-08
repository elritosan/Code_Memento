# administrador_guardados.py
class ClassAdministradorGuardados:
    def __init__(self):
        self.historial = []

    def guardar(self, memento):
        self.historial.append(memento)
        print(f"✅ Progreso guardado en la posición {len(self.historial) - 1} el {memento.get_estado()['timestamp']}.")

    def listar_guardados(self):
        """Muestra la lista de guardados disponibles con fecha y hora."""
        if not self.historial:
            print("⚠️ No hay guardados disponibles.")
            return
        print("\n📜 Lista de guardados:")
        for i, memento in enumerate(self.historial):
            estado = memento.get_estado()
            print(f"📌 [{i}] {estado['timestamp']} - Vida={estado['vida']}, Nivel={estado['nivel']}, Experiencia={estado['experiencia']}")

    def restaurar(self, indice):
        """Restaura un estado específico según el índice elegido."""
        if 0 <= indice < len(self.historial):
            print(f"🔄 Restaurando progreso desde la posición {indice} guardado en {self.historial[indice].get_estado()['timestamp']}...")
            return self.historial[indice]
        print("❌ Índice no válido. No se restauró ningún estado.")
        return None