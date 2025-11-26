import pandas as pd
import random

random.seed(42)

departments = ['Sales', 'Engineering', 'HR', 'Marketing', 'Finance']
attrition_choices = ['Yes', 'No']

data = []

for i in range(1, 1001):
    emp_id = i
    dept = random.choice(departments)
    age = random.randint(22, 60)
    
    # Salario depende un poco de la edad (experiencia)
    base_salary = 30000
    salary = base_salary + (age * random.randint(500, 1500))
    
    years_at_company = random.randint(1, 20)
    if years_at_company > (age - 20): # Corrección lógica simple
        years_at_company = age - 20
        
    # Generar Attrition (Rotación)
    # Hacemos que sea más probable irse si el salario es bajo o llevan mucho tiempo sin ascenso (simulado)
    prob_leave = 0.15
    if salary < 50000:
        prob_leave += 0.2
    if years_at_company > 5:
        prob_leave += 0.1
        
    attrition = 'Yes' if random.random() < prob_leave else 'No'
    
    data.append([emp_id, dept, age, salary, years_at_company, attrition])

df = pd.DataFrame(data, columns=['EmployeeID', 'Department', 'Age', 'Salary', 'YearsAtCompany', 'Attrition'])

df.to_csv('data/hr_data.csv', index=False)

print("¡Datos de RRHH generados en 'data/hr_data.csv'!")
print(df.head())
print("\nDistribución de Attrition:")
print(df['Attrition'].value_counts(normalize=True))
