import pandas as pd
import matplotlib.pyplot as plt

# Carga de Datos
df = pd.read_csv('data/hr_data.csv')

# Visualización primeros datos
print(df.head())

# Visualización Tipo de Dato por columna
df.info()

# Limpieza de columnas
df.columns = df.columns.str.strip()
df['Attrition'] = df['Attrition'].str.strip()
df['Department'] = df['Department'].str.strip()

# Jóvenes y Ricos
# ¿Cuántos empleados tienen menos de 30 años y ganan más de $80,000?
young_and_rich = df[(df['Age'] < 30) & (df['Salary'] > 80000)]
print(f'Empleados menores de 30 y con ingreso mayor a $80,000: {len(young_and_rich)}')

# Pérdida en Ventas
# Calcular el salario promedio de la gente que es del departamento de 'Sales' y además se fue
leavers = df[(df['Attrition'] == 'Yes') & (df['Department'] == 'Sales')]
print(leavers['Salary'].mean().round(2))

# Rango de Edad en Marketing
# Queremos saber que tan diverso es el equipo de Marketing en cuanto a edad
marketing = df[df['Department'] == 'Marketing']
age = marketing['Age']
print(f'Edad mínima: {age.min()}, edad máxima: {age.max()}')

# Clase Media
# ¿Cuál es la edad promedio de los empleados que ganan entre $60,000 y $80,000?
medium_class = df[(df['Salary'] >= 60000) & (df['Salary'] <= 80000)]
print(medium_class['Age'].mean())

# Fuerza Comercial
# Queremos saber el tamaño total de nuestra fuerza comercial (Ventas + Marketing). Cuenta cuántos empleados pertenecen a 'Sales' o 'Marketing'
employees = df[(df['Department'] == 'Sales') | (df['Department'] == 'Marketing')]
print(employees['Department'].count())

# El costo del Adiós
# Calcula cuánto nos cuesta que la gente se vaya
leavers = df[df['Attrition'] == 'Yes']
subtotal = leavers['Salary'].sum()
total = subtotal * 0.20
print(f'\nEl costo total de la fuga de cerebros es de: ${total:,.2f}')

# -----------------------------------------------------------------------------------------------------------------
# GRÁFICOS CON MATPLOTLIB
# -----------------------------------------------------------------------------------------------------------------

# Gráfico 1: Empleados por departamento
dept_counts = df['Department'].value_counts()

# Crear la figura 
plt.figure(figsize = (10, 6))

# Crear gráfico de barras
# Eje X: Nombres de departamento
# Eje Y: Cantidad de empleados por departamento
plt.bar(dept_counts.index, dept_counts.values, color = 'skyblue')

# Etiquetas y Título
plt.title('Distribución de Empleados por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Número de Empleados')

# Guardar gráfico
plt.savefig('img/employees_by_dept.png')

# Mostrar gráfico
plt.show()

# Gráfico 2: Distribución de salarios

# Crear la figura
plt.figure(figsize = (10, 6))

# bins = 20 -> Divide los salarios en 20 rangos
# edgecolor = 'black' -> dibuja un borde negro por barra para distinguir mejor 
plt.hist(df['Salary'], bins = 20, color = 'lightgreen', edgecolor = 'black')

# Etiquetas y Título
plt.title('Distribución de Salarios')
plt.xlabel('Salario')
plt.ylabel('Frecuencia (Número de Empleados)')

# Guardar gráfico
plt.savefig('img/salary_distribution.png')

# Mostrar gráfico
plt.show()

# Gráfico 3: Proporción de Attrition
attrition_counts = df['Attrition'].value_counts()

# Crear la figura
plt.figure(figsize = (10, 6))

# autopct = '%1.1f%%' muestra el porcentaje con un decimal
# startangle = 90 gira el gráfico para que empiecen desde arriba
plt.pie(attrition_counts.values, labels = attrition_counts.index, autopct = '%1.1f%%',
        startangle = 90, colors = ['lightgreen', 'salmon'])

# Título
plt.title('Proporción de Empleados que se van (Attrition)')

# Guardar gráfico
plt.savefig('img/attrition_proportion.png')

# Mostrar gráfico
plt.show()