# Definir los datos
paises = ["El Salvador", "México", "Argentina", "Japón", "Francia", "Italia", "Brasil", "Chile", "Perú", "Colombia"]
gentilicios = ["salvadoreño", "mexicano", "argentino", "japonés", "francés", "italiano", "brasileño", "chileno", "peruano", "colombiano"]
especies = ["canina", "felina", "ovina", "bovina", "equina", "porcina", "aves", "peces", "reptiles", "anfibios"]
tipos = ["lobo", "gato", "oveja", "vaca", "caballo", "cerdo", "aguila", "tiburón", "iguana", "rana"]

#Mostra la bienvenida al programa
print("-----------------------")
print("Bienvenido al programa!")
print("-----------------------")

# Mostrar mensajes indicando lo que se está haciendo
print("Por favor ingrese su nombre de usuario: ")
nombre_usuario = input()

# Capturar el tipo de dato que se quiere ingresar
print(" ¿Qué desea ingresar, un país o una especie? ")
tipo_dato = input().lower()

# Verificar el tipo de dato ingresado y solicitar la entrada correspondiente
if tipo_dato == "país":
    print(" Ingrese el nombre del país ")
    pais = input().title()
    index_pais = paises.index(pais)
    gentilicio = gentilicios[index_pais]
    print(f"El gentilicio para {pais} es {gentilicio}")
elif tipo_dato == "especie":
    print(" Ingrese el tipo de animal ")
    especie = input().lower()
    index_especie = especies.index(especie)
    tipo = tipos[index_especie]
    print(f"El tipo de animal {especie} es {tipo}")
else:
    print("Tipo de dato no reconocido.")

# Mostrar mensaje de finalización del programa
print(" El programa ha terminado.")



