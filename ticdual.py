import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import FancyBboxPatch

# Cargar el archivo GeoJSON
archivo_geojson = './data/ne_110m_admin_0_countries.json'

# Cargar el archivo GeoJSON en un DataFrame geoespacial
world = gpd.read_file(archivo_geojson)

# Crear una paleta de colores categórica con dos colores: verde y gris
cmap = ListedColormap(['#808080', '#0c267a'])

# Definir una columna 'color' con valores 0 para todos los países
world['color'] = 0

# Asignar el valor 1 a los países mencionados que deben ser verdes
paises_mencionados = ['Germany', 'Austria', 'Switzerland', 'Netherlands', 'Slovakia','China', 'Japan', 'South Korea', 'Mexico', 'Ecuador', 'Colombia', 'Peru']
world.loc[world['ADMIN'].isin(paises_mencionados), 'color'] = 1

# Configurar la figura y los ejes
fig, ax = plt.subplots(1, 1, figsize=(12, 6))
world.plot(column='color', cmap=cmap, legend=False, ax=ax)
ax.axis('off')  # Desactivar ejes

# Crear una leyenda personalizada con los nombres de los países y los títulos de los artículos asociados
legend_labels = {
    'Alemania': 'Alemania: Triad education system model for undergraduate and graduate programs in engineering',
    'Suiza y Paises bajos': 'Suiza y Paises bajos: El sistema de formación profesional suizo ¿Qué puede aprender España de Suiza?',
    'Slovakia':'Eslovakia: Moving beyond dual education framework for the skill development of ICT potentials',
    'China, Japón y Korea del sur': 'China, Japón y Korea del sur: Un análisis comparativo de los sistemas de formación profesional en Extremo Oriente',
    'Mexico, Ecuador, Perú y Colombia': 'Mexico, Ecuador, Perú y Colombia Revolución industrial 4.0: La brecha digital en Latinoamérica',
}

# Crear una leyenda personalizada con los nombres de los países y los artículos asociados
#legend_labels = {pais: f'{pais}: Artículo {i+1}' for i, pais in enumerate(paises_mencionados)}
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', label=label, markersize=10, markerfacecolor='#0c267a') for label in legend_labels.values()]

# Mostrar la leyenda en el mapa
ax.legend(handles=legend_handles, title='Países y Artículos Asociados', loc='lower right')

plt.title('Modelos de formación dual consultados')
plt.show()