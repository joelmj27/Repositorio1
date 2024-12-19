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

#Ejercico 1
elementos = ["nombre", "presupuesto", "personas_alcanzadas"]

for e in lista_campañas:
  for i in elementos:
    print(f"{i}:{e[i]}")
  print("\n")
  
#Ejericico 2
medios_utilizados = set()
for campaña in lista_campañas:
  for medio in campaña['medios']:
    medios_utilizados.add(medio)
print(medios_utilizados)

#Ejericico 3
conteo_medios={}
for campaña in lista_campañas:
  for medio in campaña["medios"]:
    if medio not in conteo_medios.keys():
      conteo_medios[medio]=1
    if medio in conteo_medios.keys():
      conteo_medios[medio]+=1

print(max(conteo_medios,key=conteo_medios.get))

print(f"El medio más usado es {max(conteo_medios,key=conteo_medios.get)} con un valor de {conteo_medios[str(max(conteo_medios,key=conteo_medios.get))]})")

#Ejericicio 4
gasto_total=0
for campañas in lista_campañas:
  gasto_total+= campañas["presupuesto"]
print( gasto_total)

#Ejercicio 5
for campañas in lista_campañas:
  conversiones = int(campañas["personas_alcanzadas"] * campañas["tasa_conversion"])
  campañas["conversiones"]=conversiones #Se asigna ya dentro de la lista el valor
for i in range(len(lista_campañas)):
  print(lista_campañas[i]["conversiones"])
  
#Ejercicio 6
mayor_tasa_conversion = 0

# Creamos una lista para almacenar el nombre de la campaña con la mayor tasa de conversión
campaña_buscada = []

# Inicializamos el índice para recorrer la lista de campañas
indice = 0

# Iteramos a través de la lista de campañas utilizando un bucle while
while indice < len(lista_campañas):
    # Obtenemos la tasa de conversión de la campaña actual en la posición 'indice'
    tasa_conversion_actual = lista_campañas[indice]["tasa_conversion"]
    
    # Comparamos la tasa de conversión actual con la mayor tasa de conversión encontrada hasta el momento
    if tasa_conversion_actual > mayor_tasa_conversion:
        # Si la tasa de conversión actual es mayor, actualizamos la mayor tasa de conversión
        mayor_tasa_conversion = tasa_conversion_actual
        # Guardamos el nombre de la campaña en la lista 'campaña_buscada'
        campaña_buscada = [lista_campañas[indice]["nombre"]]
    elif tasa_conversion_actual == mayor_tasa_conversion:
        # Si la tasa de conversión actual es igual a la mayor tasa de conversión, agregamos el nombre de la campaña a 'campaña_buscada'
        campaña_buscada.append(lista_campañas[indice]["nombre"])
    
    # Incrementamos el índice para pasar a la siguiente campaña en la lista
    indice += 1
print(campaña_buscada)



    