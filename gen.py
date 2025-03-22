import random

TAG_LIST = ["tag" + str(x) for x in range(5)]
NAME_LIST = [
    "Flavio",
    "José",
    "Daniel",
    "Adolfo",
    "María",
    "Violeta",
    "Nicolle",
    "Michelle",
]
EMAIL_LIST = ["correo" + str(x) + "@gmail.com" for x in range(20)]
FRIEND_LIST = [x for x in range(1500)]
PRODUCT_NAME_LIST = ["Producto " + str(x) for x in range(5)]


def printRandomUser(i):
    # - historial_compras [array conformado por documentos embebidos con datos de productos (string) y fecha (date)]. Al generar estos datos
    # asegúrese de generar suficiente información del producto llamado "Producto 1". Le servirá más adelante.

    name = random.choice(NAME_LIST)
    email = random.choice(EMAIL_LIST)
    points = random.randint(100, 2000)
    visits = random.randint(5, 500)
    tags = random.choices(
        TAG_LIST, weights=[1 for x in TAG_LIST], k=random.randint(2, 5)
    )
    random.shuffle(FRIEND_LIST)
    buys = [
        {"producto": random.choice(PRODUCT_NAME_LIST), "fecha": "Date()"}
        for x in range(random.randint(10, 50))
    ]

    print("{")
    print(f'nombre: "{name}",')
    print(f'email: "{email}",')
    print(f"fecha_registro: Date(),")
    print(f"puntos: {points},")
    print(f"active: true,")
    print(f'notas: "",')
    print(f"visitas: {visits},")
    print(f"amigos: {FRIEND_LIST[0:random.randint(980, 1200)]},")
    print(f"tags: {tags},")
    print(f"dirección: [],")
    print(f"preferencias: [],")
    print(f"historial_compras: {buys}")
    print("}", end="")


print("db.usuarios.insertMany([")
max = 1_000
for i in range(max):
    printRandomUser(i)
    if i < max:
        print(",")
print("])")
