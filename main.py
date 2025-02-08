# main.py
from ui import JuegoUI
import tkinter as tk
from Models.administrador_guardados import ClassAdministradorGuardados

if __name__ == "__main__":
    root = tk.Tk()
    administrador_guardados = ClassAdministradorGuardados()  # Se usa la misma instancia en toda la aplicación
    app = JuegoUI(root, administrador_guardados)  # Pasamos la instancia a la UI
    root.mainloop()