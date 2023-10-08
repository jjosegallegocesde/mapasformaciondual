import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Cargar el archivo GeoJSON
archivo_geojson = './data/south-america.geojson'

# Cargar el archivo GeoJSON en un DataFrame geoespacial
world = gpd.read_file(archivo_geojson)

# Crear una paleta de colores categórica con dos colores: gris y azul
cmap = ListedColormap(['#E9BE10','#0c267a','#808080'])

# Definir una columna 'color' con valores 'gris' para todos los países
world['color'] = 'gris'

# Asignar el valor 'azul' a Colombia
paises_mencionados = ['Ecuador', 'Peru']  # Cambia el nombre del país según tu archivo
paisColombia=['Colombia']

world.loc[world['name'].isin(paises_mencionados), 'color'] = 'azul'
world.loc[world['name'].isin(paisColombia), 'color'] = 'amarillo'

# Configurar la figura y los ejes
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
world.plot(column='color', cmap=cmap, legend=False, ax=ax)
ax.axis('off')  # Desactivar ejes

plt.title('Modelos de formación dual consultados en territorio sur americano')
plt.show()
