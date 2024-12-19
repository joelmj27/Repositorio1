lista_campañas = [
    {
        'nombre': 'Rebajas de Enero',
        'presupuesto': 35000,
        'inicio': '2023-01-02',
        'fin': '2023-01-31',
        'medios': ['Publicidad en línea', 'Redes Sociales', 'Email Marketing'],
        'segmentos_objetivo': ['Clientes regulares', 'Potenciales compradores'],
        'personas_alcanzadas': 50000,
        'tasa_conversion': 0.02
    },
    {
        'nombre': 'San Valentín',
        'presupuesto': 25000,
        'inicio': '2023-02-01',
        'fin': '2023-02-14',
        'medios': ['Redes Sociales', 'Email Marketing', 'Publicidad impresa'],
        'segmentos_objetivo': ['Parejas', 'Jóvenes'],
        'personas_alcanzadas': 30000,
        'tasa_conversion': 0.05
    },
    {
        'nombre': 'Día del Padre',
        'presupuesto': 20000,
        'inicio': '2023-06-01',
        'fin': '2023-06-15',
        'medios': ['Redes Sociales', 'Colaboraciones con influencers', 'Publicidad impresa'],
        'segmentos_objetivo': ['Jóvenes', 'Familias'],
        'personas_alcanzadas': 25000,
        'tasa_conversion': 0.03
    },
    {
        'nombre': 'Día de la Madre',
        'presupuesto': 22000,
        'inicio': '2023-04-20',
        'fin': '2023-05-10',
        'medios': ['Publicidad en línea', 'Redes Sociales', 'Email Marketing'],
        'segmentos_objetivo': ['Jóvenes', 'Familias'],
        'personas_alcanzadas': 28000,
        'tasa_conversion': 0.04
    },
    {
        'nombre': 'Día del Friki',
        'presupuesto': 18000,
        'inicio': '2023-05-20',
        'fin': '2023-05-25',
        'medios': ['Publicidad en tiendas físicas', 'Redes Sociales', 'Colaboraciones con influencers'],
        'segmentos_objetivo': ['Jóvenes'],
        'personas_alcanzadas': 20000,
        'tasa_conversion': 0.05
    },
    {
        'nombre': 'Black Friday',
        'presupuesto': 50000,
        'inicio': '2023-11-21',
        'fin': '2023-11-30',
        'medios': ['Redes Sociales', 'Email Marketing', 'Publicidad en línea'],
        'segmentos_objetivo': ['Todos los compradores'],
        'personas_alcanzadas': 100000,
        'tasa_conversion': 0.03
    },
    {
        'nombre': 'Navidad',
        'presupuesto': 60000,
        'inicio': '2023-12-01',
        'fin': '2023-12-24',
        'medios': ['Publicidad en tiendas físicas', 'Redes Sociales', 'Publicidad impresa'],
        'segmentos_objetivo': ['Todos los compradores'],
        'personas_alcanzadas': 120000,
        'tasa_conversion': 0.04
    }
]

#Ejercicio 8
from datetime import datetime
for campañas in lista_campañas:
   campañas["duracion_dias"]=(datetime.strptime(campañas['fin'], '%Y-%m-%d')-datetime.strptime(campañas['inicio'], '%Y-%m-%d')).days
for campañas in lista_campañas:
  print(campañas['nombre'], campañas['duracion_dias'])
  
#Ejercicio 9
campaña_mas_larga=("",0)
for campañas in lista_campañas:
  if campañas["duracion_dias"] > campaña_mas_larga[1]:
    campaña_mas_larga = (campañas["nombre"], campañas["duracion_dias"])
print(campaña_mas_larga)

#Ejercicio 10
for campañas in lista_campañas:
    try:
        tasa_conversion=campañas['tasa_conversion']
    except KeyError:
        print(f"Tasa de conversión no encontrada para la campaña: {campañas['nombre']}")
    else:
        print(f"Tasa de conversión de la campaña {campañas['nombre']}: {tasa_conversion}")

#Ejercicio 11
for campañas in lista_campañas:
    try:
        campañas['personas_alcanzadas']=int(campañas['personas_alcanzadas'])
    except ValueError:
        print( "el valor de personas_alcanzadas no es un número válido")
        
        
import numpy as np
