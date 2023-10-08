import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('./data/scopusgestion.csv')

# Contar la cantidad de artículos por año
articulos_por_anio = df['Year'].value_counts().sort_index()

# Crear la figura y los ejes
plt.figure(figsize=(10, 6))
plt.plot(articulos_por_anio.index, articulos_por_anio.values, marker='o', linestyle='-')

# Rellenar el área bajo la curva con color
plt.fill_between(articulos_por_anio.index, articulos_por_anio.values, color='lightblue')

# Configurar etiquetas y título
plt.xlabel('Año')
plt.ylabel('Cantidad de Artículos')
plt.title('Publicaciones asociadas a la gestión del conocimiento y la formación TIC en los últimos años')

# Configurar el eje x para mostrar solo valores enteros
plt.xticks(articulos_por_anio.index.astype(int))

# Mostrar la gráfica
plt.grid(True)
plt.show()
