import math
import pandas as pd
import matplotlib.pyplot as plt

n = 10 #int(input("¿Cuántas iteraciones desea realizar?: "))

# Vector inicial
x1 = x2 = x3 = x4 = x5 = 0.0

datos = []

datos.append([0, x1, x2, x3, x4, x5, 0])

for k in range(1, n + 1):

    x1_old, x2_old, x3_old, x4_old, x5_old = x1, x2, x3, x4, x5

    # Método de Gauss-Seidel
    x1 = (10 - (-x2 -2*x3 + x4 + 4*x5))/12
    
    x2 = (10 - (-3*x1 + 5*x3 - x4))/12
    
    x3 = (10 - (4*x1 - x2 + 3*x4 - 2*x5))/12
    
    x4 = (10 - (4*x2 - 2*x3 + 3*x5))/12
    
    x5 = (10 - (-x1 + 3*x3 + 2*x4))/12

    error = math.sqrt(
        (x1-x1_old)**2 +
        (x2-x2_old)**2 +
        (x3-x3_old)**2 +
        (x4-x4_old)**2 +
        (x5-x5_old)**2

    )

    datos.append([
        k,
        round(x1,6),
        round(x2,6),
        round(x3,6),
        round(x4,6),
        round(x5,6),
        round(error,6)
    ])

df = pd.DataFrame(
    datos,
    columns=["Iter", "x1", "x2", "x3", "x4", "x5", "Error"]
)

print(df)

# Crear imagen
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

plt.savefig("tabla_gauss_seidel.png", bbox_inches='tight')
plt.show()

print("\nImagen guardada como: tabla_gauss_seidel.png")
