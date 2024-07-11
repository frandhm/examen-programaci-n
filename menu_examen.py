from funciones import *


while True:
    limpiar()
    print("""
    Menú
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas
4. Reporte de sueldos
5. Salir           
""")
    while True:
        try:
            opc = int(input("Elija una opción: "))
            break
        except:
            print("Error! Elija una opción que este en el menú")
    
    if opc == 1:
        asignar_sueldos()
    elif opc == 2:
        clasificar_sueldos()
    elif opc == 3:
        ver_estadisticas()
    elif opc == 4:
        reporte_sueldos()
    elif opc == 5:
        salir()