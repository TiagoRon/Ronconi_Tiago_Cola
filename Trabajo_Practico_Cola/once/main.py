from cola import Queue

characters = [
    {"name": "Luke Skywalker", "planet": "Tatooine"},
    {"name": "Han Solo", "planet": "Corellia"},
    {"name": "Leia Organa", "planet": "Alderaan"},
    {"name": "Yoda", "planet": "Dagobah"},
    {"name": "Jar Jar Binks", "planet": "Naboo"},
    {"name": "Darth Vader", "planet": "Tatooine"},
    {"name": "Chewbacca", "planet": "Kashyyyk"},
    {"name": "C-3PO", "planet": "Tatooine"},
    {"name": "R2-D2", "planet": "Naboo"}
]

queue = Queue()
for character in characters:
    queue.arrive(character)

def mostrar_personajes_de_planetas(queue, planets):
    temp_queue = Queue()
    while queue.size() > 0:
        character = queue.attention()
        if character["planet"] in planets:
            print(f'{character["name"]} es de {character["planet"]}')
        temp_queue.arrive(character)
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

mostrar_personajes_de_planetas(queue, ["Alderaan", "Endor", "Tatooine"])

def mostrar_planeta_natal(queue, names):
    temp_queue = Queue()
    while queue.size() > 0:
        character = queue.attention()
        if character["name"] in names:
            print(f'{character["name"]} es de {character["planet"]}')
        temp_queue.arrive(character)
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

mostrar_planeta_natal(queue, ["Luke Skywalker", "Han Solo"])

def insertar_personaje_antes(queue, new_character, before_name):
    temp_queue = Queue()
    inserted = False
    while queue.size() > 0:
        character = queue.attention()
        if character["name"] == before_name and not inserted:
            temp_queue.arrive(new_character)
            inserted = True
        temp_queue.arrive(character)
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

new_character = {"name": "Obi-Wan Kenobi", "planet": "Stewjon"}
insertar_personaje_antes(queue, new_character, "Yoda")

def eliminar_despues_de_personaje(queue, after_name):
    temp_queue = Queue()
    found = False
    while queue.size() > 0:
        character = queue.attention()
        if found:
            found = False
            continue
        temp_queue.arrive(character)
        if character["name"] == after_name:
            found = True
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

eliminar_despues_de_personaje(queue, "Jar Jar Binks")

def mostrar_cola(queue):
    temp_queue = Queue()
    while queue.size() > 0:
        character = queue.attention()
        print(f'{character["name"]} de {character["planet"]}')
        temp_queue.arrive(character)
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

mostrar_cola(queue)
