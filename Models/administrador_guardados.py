class ClassAdministradorGuardados:
    def __init__(self):
        self.historial = []

    def guardar(self, memento):
        self.historial.append(memento)
        print(f"✅ Progreso guardado en la posición {len(self.historial) - 1} el {memento.get_estado()['timestamp']}.")

    def listar_guardados(self):
        """Devuelve una lista de los guardados disponibles con fecha y hora."""
        if not self.historial:
            print("⚠️ No hay guardados disponibles.")
            return []
        
        lista = [
            f"[{i}] {memento.get_estado()['timestamp']} - Vida={memento.get_estado()['vida']}, Nivel={memento.get_estado()['nivel']}, Experiencia={memento.get_estado()['experiencia']}"
            for i, memento in enumerate(self.historial)
        ]
        
        print("\n📜 Lista de guardados disponibles desde listar_guardados():")
        for item in lista:
            print(item)  # Verifica que la lista contenga elementos
        
        return lista

    def restaurar(self, indice):
        """Restaura un estado específico según el índice elegido."""
        if 0 <= indice < len(self.historial):
            print(f"🔄 Restaurando progreso desde la posición {indice} guardado en {self.historial[indice].get_estado()['timestamp']}...")
            return self.historial[indice]
        print("❌ Índice no válido. No se restauró ningún estado.")
        return None