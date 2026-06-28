import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n = 10 #int(input("¿Cuántas iteraciones desea realizar?: "))

# Vector inicial
x1 = x2 = x3 = x4 = x5 = 0.0

datos = []
datos.append([0, x1, x2, x3, x4, x5,0])

for k in range(1, n + 1):

    nx1 = (10 - (-x2 -2*x3 + x4 + 4*x5))/12
    nx2 = (10 - (-3*x1 + 5*x3 - x4))/12
    nx3 = (10 - (4*x1 - x2 + 3*x4 - 2*x5))/12
    nx4 = (10 - (4*x2 - 2*x3 + 3*x5))/12
    nx5 = (10 - (-x1 + 3*x3 + 2*x4))/12


    error = math.sqrt(
        (nx1-x1)**2 +
        (nx2-x2)**2 +
        (nx3-x3)**2 +
        (nx4-x4)**2 +
        (nx5-x5)**2
    )

    datos.append([
        k,
        round(nx1,6),
        round(nx2,6),
        round(nx3,6),
        round(nx4,6),
        round(nx5,6),
        round(error,6)
    ])

    x1, x2, x3, x4, x5 = nx1, nx2, nx3, nx4, nx5

# Crear DataFrame
df = pd.DataFrame(
    datos,
    columns=["Iter", "x1", "x2", "x3", "x4", "x5", "Error"]
)

print(df)

# Crear imagen de la tabla
fig, ax = plt.subplots(figsize=(10, len(df)*0.5 + 1))
ax.axis('off')

tabla = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc='center'
)

tabla.auto_set_font_size(False)
tabla.set_fontsize(10)
tabla.scale(1.2, 1.5)

plt.savefig("tabla_jacobi.png", bbox_inches='tight')
plt.show()

print("\nImagen guardada como: tabla_jacobi.png")