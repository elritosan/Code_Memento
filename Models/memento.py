# Models\memento.py
from datetime import datetime

class ClassMemento:
    def __init__(self, vida, nivel, experiencia):
        self._vida = vida
        self._nivel = nivel
        self._experiencia = experiencia
        self._timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fecha y hora del guardado

    def get_estado(self):
        return {
            "vida": self._vida,
            "nivel": self._nivel,
            "experiencia": self._experiencia,
            "timestamp": self._timestamp
        }