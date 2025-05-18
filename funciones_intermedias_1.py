#1. Actualizar valores en diccionarios y listas
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
indice_cancun = ciudades["México"].index("Cancún")
ciudades["México"][indice_cancun] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

#2. Crear una función que reciba una lista de diccionarios y los imprima
def iterarDiccionario(lista):
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"{llave} - {valor}")
        print()

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)

#3. Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
iterarDiccionario2("nombre", cantantes)

#4. Iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
    for clave, valores in diccionario.items():
        # Imprime la cantidad de elementos y la clave en mayúsculas
        print(f"{len(valores)} {clave.upper()}")
        # Imprime cada valor de la lista en una línea nueva
        for valor in valores:
            print(valor)
        print()  # Línea en blanco para separar cada sección

# Ejemplo de uso
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)