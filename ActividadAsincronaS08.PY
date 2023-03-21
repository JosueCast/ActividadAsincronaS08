print("Bienvenido al programa")
#Declaracion de varaibles de humanos
pais1 = str("EL SALVADOR")
pais2 = str("NICARAGUA")
pais3 = str("COSTA RICA")
pais4 = str("PANAMA")
pais5 = str("COLOMBIA")
pais6 = str("CHILE")
pais7 = str ("CANADA")
pais8 = str("MEXICO")
pais9 = str("BRASIL")
pais10 = str("PERU")
#declaracion de variables de animales
espe1 = "mamiferos"
espe2 = "insectos"
espe3 = "Arañas y Alacranes"
espe4 = "cangrejos y Camarones"
espe5 = "reptiles"
espe6 = "aves"
espe7 = "peces"
espe8 = "ranas y sapos"
espe9 = "ciempies y milpies"
espe10 = "estrellas y erizos"
#pidiendo nombre de usuario para un mensaje de respuesta
usuario = input("Ingrese su Nombre -> ")
#Mostrando menu de opciones de paise y humanos
menu1 = input('''
            \tMenu
            1- Pais
            2- Animales
            
            
            Elija una Opción del Menu -> ''' ).lower()

#evaluando la opcion que agrego el usuario mediante el teclado
if menu1 == "pais" or menu1 == "1":
    menu2 = input(f'''
                \tMenu
                1- {pais1}
                2- {pais2}
                3- {pais3}
                4- {pais4}
                5- {pais5}
                6- {pais6}
                7- {pais7}
                8- {pais8}
                9- {pais9}
                10- {pais10}
            
                Ingrese un Pais -> ''').upper()
#evaluadon los gentilicios con forme al pais que escogio el usuario
    if menu2 == pais1 or menu2 == '1':
        #se evalua y lo mostramos mediante un print() al usuario utilizando la primera varaible usuario que se pidio mendiante el teclado
        print(f"{usuario} usted es de {pais1} el gentilicio de su pais es Salvadoreño ")
    elif menu2 == pais2 or menu2 == '2':
        print(f"{usuario} usted es de {pais2} el gentilicio de su pais es: Nicaraguense ")
    elif menu2 == pais3 or menu2 == '3':
        print(f"{usuario} Usted es del {pais3} el gentilicoo de su pais es: costarricense ")
    elif menu2 == pais4 or menu2 == '4':
        print(f"{usuario} Usted es de {pais4} el gentilicio de su pais es: Panameño ")
    elif menu2 == pais5 or menu2 == '5':
        print(f"{usuario} Usted eligio {pais5} el genticilio de su pais es: Colombiano ")
    elif menu2 == pais6 or menu2 == '6':
        print(f"{usuario} Usted eligio {pais6} el gentilicio de su pais es: Chileno ")
    elif menu2 == pais7 or menu2 == '7':
        print(f"{usuario} Usted es del {pais7} el gentilicoo de su pais es: Canadiense ")
    elif menu2 == pais8 or menu2 == '8':
        print(f"{usuario} Usted es de {pais8} el gentilicio de su pais es: Mexicano ")
    elif menu2 == pais9 or menu2 == '9':
        print(f"{usuario} Usted eligio {pais9} el genticilio de su pais es: Brasileño ")
    elif menu2 == pais10 or menu2 == '10':
        print(f"{usuario} Usted eligio {pais10} el gentilicio de su pais es: Peruano ")
    #si no se encuentra el pais  la opcion no estra disponible
    else:
        print("La opcion no esta disponible")
#evaluando datos ingresado por el usuario mendiante el teclado tipo de animal
elif menu1 == "animales" or menu1 == "2":
    #Mostrando una lista de las tipos de animales que estan
        menu2 = input(f'''
                        \tMenu de Especies 
                        1- {espe1}
                        2- {espe2}
                        3- {espe3}
                        4- {espe4}
                        5- {espe5}
                        6- {espe6}
                        7- {espe7}
                        8- {espe8}
                        9- {espe9}
                        10- {espe10}
                         
                          Ingrese que tipo de Especie quiere saber -> ''').lower()
        #evaluando el dato ingresado o la opcion del usuario
        if menu2 == espe1 or menu2 == "1":
            #se evalua y lo mostramos mediante un print() al usuario utilizando la primera varaible usuario que se pidio mendiante el teclado
            print(usuario + " Algunos animales dentro de " + espe1 + " son: 'León' 'Zebra' 'Canguro' 'Delfines'")
        elif menu2 == espe2 or menu2 == "2":
            print(usuario + " Algunos animales dentro de " + espe2 + " son : 'Abejas' 'Cucarachas' 'Saltamontes' 'Mariposas' ")
        elif menu2 == espe3 or menu2 == "3":
            print(usuario + " Algunos animales dentro de " + espe3 + " son : 'Araña orden Araneae' 'Arañas patonas sin cintura' 'alacrán de Morelos' 'Alacran de cola negra' ")
        elif menu2 == espe4 or menu2 == "4":
            print(usuario + " Algunos animales dentro de " + espe4 + " son : 'Centolla Patagonica' 'Cangrejo moro' 'Camarón posidonia' 'Camaron quisquilla' ")
        elif menu2 == espe5 or menu2 == "5":
            print(usuario + " Algunos animales dentro de " + espe5 + " son : 'Tortuga' 'Caiman' 'Cocodrilo' 'Camaleon' ")
        elif menu2 == espe6 or menu2 == "6":
            print(usuario + " Algunos animales dentro de " + espe6 + " son : 'Ganzo' 'Lechuza' 'Golondrina' 'Tucán' ")
        elif menu2 == espe7 or menu2 == "7":
            print(usuario + " Algunos animales dentro de " + espe7 + " son : 'Anguilas' 'Pez dorado' 'Mojarra' 'Trucha' ")
        elif menu2 == espe8 or menu2 == "8":
            print(usuario + " Algunos animales dentro de " + espe8 + " son : 'Rana Campestre' 'Rana Patilar' 'Rana de Cristal' 'Rana Dorada' ")
        elif menu2 == espe9 or menu2 == "9":
            print(usuario + " Algunos animales dentro de " + espe9 + " son : 'Scolopendromorpha' 'Scutigeromorpha' 'Geophilomorpha' 'Lithobiomorpha' ")
        elif menu2 == espe10 or menu2 == "10":
            print(usuario + " Algunos animales dentro de " + espe10 + " son : 'Asterias rubens' 'Luidia ciliaris' 'Tabaquera ' 'Erizo diadema' ")
        # si su dato ingresado no se encuentra no se se puede mostra una opcion si 
        else:
            print("La opcion seleccionada no esta disponible")

else:
    print("La opcion no esta disponible")
#finalizando el programa
print("Fin del programa :)")
        
  
