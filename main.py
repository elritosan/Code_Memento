# main.py
from Models.jugador import ClassJugador
from Models.administrador_guardados import ClassAdministradorGuardados

# Instancias
jugador = ClassJugador()
administrador = ClassAdministradorGuardados()

# Guardamos estados iniciales
jugador.mostrar_estado()
administrador.guardar(jugador.guardar_progreso())  # Estado 0

# Jugador combate y guarda nuevos estados con fecha y hora
jugador.combatir()
jugador.mostrar_estado()
administrador.guardar(jugador.guardar_progreso())  # Estado 1

jugador.combatir()
jugador.mostrar_estado()
administrador.guardar(jugador.guardar_progreso())  # Estado 2

jugador.combatir()
jugador.mostrar_estado()
administrador.guardar(jugador.guardar_progreso())  # Estado 3

# 🎯 Listamos los guardados disponibles con fecha y hora
administrador.listar_guardados()

# 📌 Permitir al usuario restaurar un guardado específico
indice = int(input("\n🔄 Introduce el número de guardado a restaurar: "))
estado_previo = administrador.restaurar(indice)

if estado_previo:
    jugador.cargar_progreso(estado_previo)
    print("\n✅ Progreso restaurado:")
    jugador.mostrar_estado()