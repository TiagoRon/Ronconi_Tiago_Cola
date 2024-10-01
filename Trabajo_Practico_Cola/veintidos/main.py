from cola import Queue

characters = [
    {"nombre": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"nombre": "Steve Rogers", "superheroe": "Capitan America", "genero": "M"},
    {"nombre": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"nombre": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"nombre": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"nombre": "Thor Odinson", "superheroe": "Thor", "genero": "M"},
    {"nombre": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"},
]

queue = Queue()
for character in characters:
    queue.arrive(character)

def obtener_personaje_capitana_marvel(queue):
    while queue.size() > 0:
        character = queue.attention()
        if character["superheroe"] == "Capitana Marvel":
            print(f'El personaje de Capitana Marvel es: {character["nombre"]}')

def mostrar_superheroes_femeninos(queue):
    print("Superheroes femeninos:")
    while queue.size() > 0:
        character = queue.attention()
        if character["genero"] == "F":
            print(f'Nombre: {character["superheroe"]}')

def mostrar_personajes_masculinos(queue):
    print("Personajes masculinos:")
    while queue.size() > 0:
        character = queue.attention()
        if character["genero"] == "M":
            print(f'Nombre: {character["nombre"]}')

def obtener_superheroe_scott_lang(queue):
    while queue.size() > 0:
        character = queue.attention()
        if character["nombre"] == "Scott Lang":
            print(f'El superheroe de Scott Lang es: {character["superheroe"]}')

def mostrar_datos_con_s(queue):
    print("Datos de superheroes o personajes cuyos nombres comienzan con S:")
    while queue.size() > 0:
        character = queue.attention()
        if character["nombre"].startswith("S"):
            print(f'Nombre: {character["nombre"]}, Superheroe: {character["superheroe"]}, Genero: {character["genero"]}')

def verificar_personaje_carol_danvers(queue):
    encontrado = False
    while queue.size() > 0:
        character = queue.attention()
        if character["nombre"] == "Carol Danvers":
            print(f'Carol Danvers es {character["superheroe"]}')
            encontrado = True
            break
    if not encontrado:
        print("Carol Danvers no se encuentra en la cola.")


obtener_personaje_capitana_marvel(queue)
queue = Queue()
for character in characters:
    queue.arrive(character)
mostrar_superheroes_femeninos(queue)
queue = Queue()
for character in characters:
    queue.arrive(character)
mostrar_personajes_masculinos(queue)
queue = Queue()
for character in characters:
    queue.arrive(character)
obtener_superheroe_scott_lang(queue)
queue = Queue()
for character in characters:
    queue.arrive(character)
mostrar_datos_con_s(queue)
queue = Queue()
for character in characters:
    queue.arrive(character)
verificar_personaje_carol_danvers(queue)
