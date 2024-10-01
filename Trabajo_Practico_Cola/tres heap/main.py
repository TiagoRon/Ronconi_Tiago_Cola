from heap_max import HeapMax
from operacion import Operacion

PRIORIDAD_NIVEL_3 = 3
PRIORIDAD_NIVEL_2 = 2
PRIORIDAD_NIVEL_1 = 1

cola_prioridad = HeapMax()

operaciones_iniciales = [
    Operacion('Lider Supremo Snoke', 'Atacar la base rebelde', '08:00', 100),
    Operacion('Kylo Ren', 'Buscar a Rey en el planeta Jakku', '09:00', 50),
    Operacion('Capitan Phasma', 'Supervisar el entrenamiento de Stormtroopers', '10:00', 20),
    Operacion('Capitan Phasma', 'Revisar los sistemas de defensa', '11:00', 30),
    Operacion('Capitan Phasma', 'Realizar patrullaje en la base', '12:00', 25),
    Operacion('Capitan Phasma', 'Asegurar los suministros', '13:00', 15),
    Operacion('General Hux', 'Monitorear comunicaciones', '14:00'),
    Operacion('General Hux', 'Revision de mantenimiento', '15:00'),
    Operacion('General Hux', 'Organizar las tropas en la base Starkiller', '16:00'),
    Operacion('General Hux', 'Inspeccionar hangar', '17:00', 10)
]

for op in operaciones_iniciales:
    if op.encargado in ['Lider Supremo Snoke', 'Kylo Ren']:
        prioridad = PRIORIDAD_NIVEL_3
    elif op.encargado == 'Capitan Phasma':
        prioridad = PRIORIDAD_NIVEL_2
    else:
        prioridad = PRIORIDAD_NIVEL_1
    cola_prioridad.arrive(op, prioridad)

def atender_operacion(cola, contador):
    operacion = cola.attend()
    if operacion:
        operacion_obj = operacion[1]
        print(f"Atendiendo operacion #{contador}: {operacion_obj}\n")
    else:
        print("No hay operaciones en la cola.\n")
    return operacion

contador_atencion = 0

while not cola_prioridad.esta_vacio():
    contador_atencion += 1
    atender_operacion(cola_prioridad, contador_atencion)
    
    if contador_atencion == 5:
        print("Agregando operacion de Capitan Phasma: Revision de intrusos en el hangar B7 (25 Stormtroopers)\n")
        nueva_op_phasma = Operacion('Capitan Phasma', 'Revision de intrusos en el hangar B7', '18:00', 25)
        cola_prioridad.arrive(nueva_op_phasma, PRIORIDAD_NIVEL_2)
    
    if contador_atencion == 6:
        print("Agregando operacion de Snoke: Destruir el planeta Takodana (200 Stormtroopers)\n")
        nueva_op_snoke = Operacion('Lider Supremo Snoke', 'Destruir el planeta Takodana', '19:00', 200)
        cola_prioridad.arrive(nueva_op_snoke, PRIORIDAD_NIVEL_3)
