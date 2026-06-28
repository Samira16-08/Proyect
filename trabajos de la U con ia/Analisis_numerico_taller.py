import numpy as np
import matplotlib.pyplot as plt

#Problem data
T0 = 75         #Temperatura inicial del cafe
Ta = 24         #Temperatura ambiente
k =  0.1659     #Constante de enfriamiento
T_euler = [T0]

#Time 0 to 15 mins
t = np.arange(0, 16, 1)

#Analitical solution
T = Ta + (T0 - Ta) * np.exp(-k * t)

#Euler method
for i in range(1, len(t)):
    T_actual = T_euler[i-1]
    T_new = T_actual - k * (T_actual - Ta) * 1
    T_euler.append(T_new)

#Error
Ev = abs((T - T_euler)/T)       


#Show results terminal
print("i |  t (min) | T (°C) - Analitica | T(°C) - Euler | Error verdadero")
print("---------------------------------------------------------------")
for i in range(len(t)):
    print(f"{i} | {t[i]}         |    {round(T[i], 5)}    |    {round(T_euler[i], 5)}      |      {round(Ev[i], 5)}")
    


#Tabla png
fig, ax =  plt.subplots()
ax.axis("off")

tabla_datos = []
for i in range(len(t)):
    tabla_datos.append([i, t[i], round(T[i], 5), round(T_euler[i], 5), round(Ev[i], 5)])

tabla = ax.table(cellText=tabla_datos, colLabels=["i", "t", "T (°C) - Analitica", "T(°C) - Euler", "Error verdadero"], loc="center")

tabla.auto_set_font_size(False)
tabla.set_fontsize(10)
tabla.scale(1.2, 1.2)

plt.savefig("Tabla.png", bbox_inches="tight")
plt.show()

#Grafica png
plt.plot(t, T, label = "Analitica", marker = "o")
plt.plot(t, T_euler, label = "Euler", marker = "s")

plt.xlabel("Tiempo (min)")
plt.ylabel("Temperatura (°C)")
plt.title("Enfriamiento del cafe")

plt.legend()
plt.grid()

plt.savefig("Grafica.png")
plt.show()
