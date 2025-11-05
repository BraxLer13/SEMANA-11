from modelo import ModeloGeneral
from vista import VistaSesion
from controlador import Controlador

# ==================== ZONA DE CÓDIGO PRINCIPAL ====================

# Crear instancia del modelo general
objModelo = ModeloGeneral()

# Crear instancia de la vista de sesión
objVista = VistaSesion()

# Crear el controlador que maneja la interacción entre modelo y vista
objControlador = Controlador(objVista, objModelo)

# Ejecutar la ventana principal de la vista de sesión
objVista.ventana.mainloop()