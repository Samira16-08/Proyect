import numpy as np
import matplotlib.pyplot as plt

#FUNCION
def f(x):
    return np.exp(x) + 2**(-x) + 2*np.cosd(x) - 6


# BISECCIÓN
def biseccion_tabla(xl, xu, tol=1e-3):
    xr_ant = xl
    i = 0
    tabla = []

    while i < 100: 
        xr = (xl + xu) / 2

        fxl = f(xl)
        fxu = f(xu)
        fxr = f(xr)

        if i == 0:
            error = 0
        else:
            error = abs((xr - xr_ant) / xr)

        tabla.append([i, xl, xu, xr, fxl, fxu, fxr, error])

        if i != 0 and error < tol:
            break

        if fxl * fxr < 0:
            xu = xr
        else:
            xl = xr

        xr_ant = xr
        i += 1

    return tabla


#IMAGEN TABLA BISECCION
def guardar_tabla(tabla, nombre="tabla_biseccion.png"):
    columnas = ["i", "xl", "xu", "xr", "f(xl)", "f(xu)", "f(xr)", "error"]

    # Redondear datos
    tabla_redondeada = [[f"{v:.6f}" if isinstance(v, float) else v for v in fila] for fila in tabla]

    fig, ax = plt.subplots()
    ax.axis('off')

    tabla_plot = ax.table(
        cellText=tabla_redondeada,
        colLabels=columnas,
        loc='center'
    )

    tabla_plot.auto_set_font_size(False)
    tabla_plot.set_fontsize(8)
    tabla_plot.auto_set_column_width(col=list(range(len(columnas))))

    plt.savefig(nombre, bbox_inches='tight')
    plt.show()

#IMAGEN TABLA FALSA POSICION
def falsa_posicion_tabla(xl, xu, tol=1e-3):
    xr_ant = xl
    i = 0
    tabla = []

    while i < 100:
        fxl = f(xl)
        fxu = f(xu)

        xr = xu - (fxu * (xl - xu)) / (fxl - fxu)
        fxr = f(xr)

        if i == 0:
            error = 0
        else:
            error = abs((xr - xr_ant) / xr)

        tabla.append([i, xl, xu, xr, fxl, fxu, fxr, error])

        if i != 0 and error < tol:
            break

        if fxl * fxr < 0:
            xu = xr
        else:
            xl = xr

        xr_ant = xr
        i += 1

    return tabla

# EJECUCIÓN
tabla_bis = biseccion_tabla(1, 2)
guardar_tabla(tabla_bis, "biseccion.png")
tabla_fp = falsa_posicion_tabla(1, 2)
guardar_tabla(tabla_fp, "falsa_posicion.png")