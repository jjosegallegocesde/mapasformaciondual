import matplotlib.pyplot as plt

# Datos
porcentaje_desempleados = 23.4
porcentaje_empleados = 76.6

# Etiquetas para las categorías
categorias = ['Jóvenes Desempleados', 'Jóvenes Empleados']

# Valores correspondientes a cada categoría
valores = [porcentaje_desempleados, porcentaje_empleados]

# Colores personalizados para cada segmento del gráfico
colores = ['#E9BE10', '#1E2070']

# Crear el gráfico de pastel
plt.figure(figsize=(8, 8))
plt.pie(valores, labels=categorias, colors=colores, autopct='%1.1f%%', startangle=140)
plt.title('Situación de empleo juvenil para 2022')

# Mostrar el gráfico
plt.axis('equal')  # Para que el gráfico sea un círculo en lugar de una elipse
plt.show()
