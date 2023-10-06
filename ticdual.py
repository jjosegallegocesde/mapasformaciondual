import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Cargar el archivo GeoJSON
archivo_geojson = './data/ne_110m_admin_0_countries.json'

# Cargar el archivo GeoJSON en un DataFrame geoespacial
world = gpd.read_file(archivo_geojson)

# Crear una paleta de colores categórica con dos colores: verde y gris
cmap = ListedColormap(['#808080','#00FF00'])

# Definir una columna 'color' con valores 0 para todos los países
world['color'] = 0

# Asignar el valor 1 a los países mencionados que deben ser verdes
paises_mencionados = ['Germany', 'Austria', 'Switzerland', 'Netherlands', 'China', 'Japan', 'Korea, South', 'Mexico', 'Ecuador', 'Colombia', 'Peru']
world.loc[world['ADMIN'].isin(paises_mencionados), 'color'] = 1

# Visualizar los límites de los países con colores personalizados
world.plot(column='color', cmap=cmap, legend=False, figsize=(12, 6))
plt.title('Modelos de formación dual consultados')
plt.axis('off')  # Desactivar ejes
plt.show()
