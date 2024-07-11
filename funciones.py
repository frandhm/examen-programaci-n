import random, time, os, msvcrt

sueldos_800 = []
sueldos_800o2m = []
sueldos_2m_mas = []
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos_aleatorios = []
sueldos = []

def limpiar():
    os.system("cls")

def esperar(a):
    time.sleep(a)

def esperar_tecla():
    msvcrt.getch()

def numero_aleatorio():
    aleatorio = random.randint(300000,2500000)
    return aleatorio

def asignar_sueldos():
    limpiar()
    print("Asignar sueldos aleatorios")
    
    for i in range(0,10):
        num_random = numero_aleatorio()
        sueldos_aleatorios.append(num_random)
        trabajadores_con_sueldo = [trabajadores[i],num_random]
        if num_random < 800000:
            sueldos_800.append(trabajadores_con_sueldo)
        elif num_random >= 800000 and num_random <= 2000000:
            sueldos_800o2m.append(trabajadores_con_sueldo)
        elif num_random > 2000000:
            sueldos_2m_mas.append(trabajadores_con_sueldo)
        sueldos.append(trabajadores_con_sueldo)
    esperar(1)
    print("Sueldos asignado con éxito")
    esperar(1)
    print("Presione una tecla para continuar")
    esperar_tecla()

def clasificar_sueldos():
    limpiar()
    if not sueldos:
        print("Error no hay sueldos! Primero asigne sueldos en la opción 1")
        esperar(2)
    else:
        print("Clasificar sueldos")
        print(f"\nSueldos menores a 800.000 Total = {len(sueldos_800)}")
        for i in range(len(sueldos_800)):
            print(f"""
    Nombre empleado     sueldo
    {sueldos_800[i][0]}     {sueldos_800[i][1]}    
    """)
        print(f"\nSueldos de $800.000 a 2.000.000 Total = {len(sueldos_800o2m)}")
        for i in range(len(sueldos_800o2m)):
            print(f"""      
    Nombre empleado     sueldo
    {sueldos_800o2m[i][0]}     {sueldos_800o2m[i][1]} 
    """)
        print(f"Sueldos mayores a 2.000.000 Total = {len(sueldos_2m_mas)}")
        for i in range(len(sueldos_2m_mas)):
            print(f"""
    Nombre empleado     sueldo
    {sueldos_2m_mas[i][0]}     {sueldos_2m_mas[i][1]} 
    """)    
        print(f"Total sueldos: {sum(sueldos_aleatorios)}")
        print("Presione una tecla para continuar")
        esperar_tecla()

def ver_estadisticas():
    limpiar()
    if not sueldos:
        print("Error no hay sueldos! Primero asigne sueldos en la opción 1")
        esperar(2)
    else:
        sueldo_mayor = []
        promedio = 0
        media_geometrica = 1
        print("Ver estadísticas")
        for i in range(len(sueldos)):
            if not sueldo_mayor:
                sueldo_mayor.append(sueldos_aleatorios[i])
            else:
                if sueldos_aleatorios[i] > sueldo_mayor[0]:
                    sueldo_mayor.insert(0,sueldos_aleatorios[i])
        for i in range(len(sueldo_mayor)):
            promedio += sueldo_mayor[i]
            media_geometrica *= sueldo_mayor[i]
        promedio /= len(sueldo_mayor)
        print(f"\nsueldo más alto: {sueldo_mayor[0]}\nSueldo más bajo: {sueldo_mayor[-1]}\nPromedio sueldos: {promedio}\nMedia geométrica: {media_geometrica**0.1}")    
        print("Presione una tecla para continuar")
        esperar_tecla()
def reporte_sueldos():
    limpiar()
    if not sueldos:
        print("Error no hay sueldos! Primero asigne sueldos en la opción 1")
        esperar(2)
    else:
        descuento_s = .07
        descuento_a = .12
        print("Reporte sueldos")

        for i in range(len(sueldos)):
            desA_sueldos = sueldos[i][1]
            desS_sueldos = sueldos[i][1]
            desS_sueldos -= (sueldos[i][1]*descuento_s)
            desA_sueldos -= (sueldos[i][1]*descuento_a)
            liquido = sueldos[i][1] -(desS_sueldos + desA_sueldos)
            print(f"""
    Nombre Empleado     Sueldo Base     Descuento Salud     Descuento AFP       Sueldo Liquido
    {sueldos[i][0]}     {sueldos[i][1]}     {desS_sueldos}    {desA_sueldos}    {liquido}                   
    """)
        esperar_tecla()

def salir():
    limpiar()
    print("Finalizando programa...")
    print("\nDesarrollado por Francisco Hernández\nRUT: 21990870-9")
    exit()