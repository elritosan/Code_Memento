# ui.py
import tkinter as tk
from tkinter import messagebox
from Models.jugador import ClassJugador
from Models.administrador_guardados import ClassAdministradorGuardados

class JuegoUI:
    def __init__(self, root, administrador_guardados):
        self.root = root
        self.root.title("Juego de Aventuras - Memento")
        self.jugador = ClassJugador()
        self.administrador = administrador_guardados  # Se usa la instancia global

        # Marco principal
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        # Estado del jugador
        self.estado_label = tk.Label(self.frame, text=self.get_estado(), font=("Arial", 12))
        self.estado_label.pack()

        # Botón para combatir
        self.combatir_btn = tk.Button(self.frame, text="⚔️ Combatir", command=self.combatir, font=("Arial", 12))
        self.combatir_btn.pack(pady=5)

        # Botón para guardar progreso
        self.guardar_btn = tk.Button(self.frame, text="💾 Guardar Progreso", command=self.guardar_progreso, font=("Arial", 12))
        self.guardar_btn.pack(pady=5)

        # Botón para restaurar progreso
        self.restaurar_btn = tk.Button(self.frame, text="🔄 Restaurar Progreso", command=self.mostrar_guardados, font=("Arial", 12))
        self.restaurar_btn.pack(pady=5)

    def get_estado(self):
        return f"💾 Vida: {self.jugador.vida} | Nivel: {self.jugador.nivel} | Experiencia: {self.jugador.experiencia}"

    def actualizar_estado(self):
        self.estado_label.config(text=self.get_estado())

    def combatir(self):
        self.jugador.combatir()
        self.actualizar_estado()
        messagebox.showinfo("Combate", "⚔️ Has peleado y ganado experiencia!")

    def guardar_progreso(self):
        self.administrador.guardar(self.jugador.guardar_progreso())
        messagebox.showinfo("Guardado", "✅ Progreso guardado exitosamente!")

    def mostrar_guardados(self):
        """Carga los guardados antes de abrir la ventana emergente"""
        self.administrador.listar_guardados()  # Forzar actualización en la consola

        guardados = self.administrador.listar_guardados()
        if not guardados:
            messagebox.showwarning("Restaurar", "⚠️ No hay guardados disponibles.")
            return

        # Ventana emergente para elegir un guardado
        ventana_guardados = tk.Toplevel(self.root)
        ventana_guardados.title("Seleccionar un guardado")
        tk.Label(ventana_guardados, text="Selecciona un guardado:", font=("Arial", 12)).pack()

        for i, guardado in enumerate(guardados):
            btn_guardado = tk.Button(
                ventana_guardados, text=guardado, command=lambda idx=i: self.restaurar_progreso(idx, ventana_guardados)
            )
            btn_guardado.pack(pady=2)

    def restaurar_progreso(self, indice, ventana):
        estado_previo = self.administrador.restaurar(indice)
        if estado_previo:
            self.jugador.cargar_progreso(estado_previo)
            self.actualizar_estado()
            messagebox.showinfo("Restaurado", "✅ Progreso restaurado exitosamente!")
        ventana.destroy()