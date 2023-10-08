import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV
data = pd.read_csv('./data/scopustic.csv')

# Convertir la columna "Year" a enteros
data['Year'] = data['Year'].astype(int)

# Contar la cantidad de artículos por año
articulos_por_año = data['Year'].value_counts().sort_index()

# Crear un DataFrame con los datos
df = pd.DataFrame({'Año': articulos_por_año.index, 'Cantidad de Artículos': articulos_por_año.values})

# Crear un mapa de calor
plt.figure(figsize=(10, 6))
heatmap_data = df.pivot_table(index='Año', values='Cantidad de Artículos', aggfunc='sum')
sns.heatmap(heatmap_data, cmap='Greens', annot=True, fmt='d', linewidths=0.5)
plt.xlabel('Año')
plt.ylabel('Año')
plt.title('Mapa de Calor de la cantidad de artículos por año temática: formación dual y enseñanza de TIC')
plt.tight_layout()

# Mostrar el mapa de calor
plt.show()
