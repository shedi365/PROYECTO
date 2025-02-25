# Configuración inicial
rutas_nacionales = {
    "Porlamar - Caracas": 50, "Caracas - Porlamar": 50,
    "Puerto Ordaz - Caracas": 45, "Caracas - Puerto Ordaz": 45,
    "Maracaibo - Caracas": 80, "Caracas - Maracaibo": 80,
    "El Vigla - Caracas": 75, "Caracas - El Vigla": 75,
    "Barcelona - Caracas": 30, "Caracas - Barcelona": 30,
    "La Fría - Caracas": 60, "Caracas - La Fría": 60
}

rutas_internacionales = {
    "Bogotá - Caracas": 499, "Caracas - Bogotá": 499,
    "Curazao - Caracas": 400, "Caracas - Curazao": 400,
    "Santo Domingo - Caracas": 700, "Caracas - Santo Domingo": 700,
    "La Romana - Caracas": 650, "Caracas - La Romana": 650
}

reporte = {
    "total_boletos": 0,
    "ingresos_clase": {"Primera": 0, "Segunda": 0, "Tercera": 0},
    "ingresos_tipo": {"Nacional": 0, "Internacional": 0},
    "ingresos_ruta": {},
    "servicios_adicionales": 0
}

# Bucle principal
ejecutando = True
while ejecutando:
    # Simulación de limpieza de pantalla
    print("\n" * 50)
    
    print("\n=== LASER Airlines ===")
    print("1. Comprar boleto")
    print("2. Ver reporte del sistema")
    print("3. Salir")
    opcion = input("\nSeleccione una opción: ").strip()

    if opcion == "1":
        print("\n" * 50)
        print("\n--- COMPRAR BOLETO ---\n")

# Validar número de boletos
        while True:
            try:
                num_boletos = int(input("Número de boletos a comprar: "))
                if num_boletos > 0:
                    break
                print("Error: Debe ser al menos 1 boleto.")
            except:
                print("Error: Ingrese un número válido.")
        
        total_pagar = 0
        
        for _ in range(num_boletos):
            print(f"\nBoleto #{_ + 1}")
            
            # Nombre
            nombre = input("Nombre del pasajero: ").strip()
            
            # Cédula
            while True:
                cedula = input("Cédula (V/E): ").upper()
                if cedula in ("V", "E"):
                    break
                print("Error: Ingrese V o E.")
            
            # Edad
            while True:
                try:
                    edad = int(input("Edad del pasajero: "))
                    if edad >= 18:
                        break
                    print("Error: El pasajero debe ser mayor de 18 años.")
                except:
                    print("Error: Ingrese un número válido.")
            
            # Clase
            while True:
                clase = input("Clase (1. Primera, 2. Segunda, 3. Tercera): ").strip()
                if clase in ("1", "2", "3"):
                    if clase == "3" and edad >= 60:
                        print("Error: Tercera clase no disponible para mayores de 60 años.")
                        continue
                    clase_nombre = ["Primera", "Segunda", "Tercera"][int(clase)-1]
                    break
                print("Error: Opción no válida.")
 # Tipo de boleto
            while True:
                tipo = input("Tipo (N. Nacional, I. Internacional): ").upper()
                if tipo in ("N", "I"):
                    tipo_nombre = "Nacional" if tipo == "N" else "Internacional"
                    break
                print("Error: Ingrese N o I.")
            
            # Ruta y precio
            precio_base = 0
            while True:
                if tipo_nombre == "Nacional":
                    print("Rutas nacionales disponibles:")
                    for ruta in rutas_nacionales:
                        print(f"- {ruta}")
                    ruta = input("Ruta: ").strip()
                    if ruta in rutas_nacionales:
                        precio_base = rutas_nacionales[ruta]
                        break
                else:
                    print("Rutas internacionales disponibles:")
                    for ruta in rutas_internacionales:
                        print(f"- {ruta}")
                    ruta = input("Ruta: ").strip()
                    if ruta in rutas_internacionales:
                        precio_base = rutas_internacionales[ruta] * 2
                        break
                print("Error: Ruta no válida.")
            
            # Descuentos
            if edad < 12 or edad >= 60:
                precio = precio_base * 0.9
            else:
                precio = precio_base
            
            # Servicios adicionales
            servicios = input("¿Servicios adicionales? (S/N): ").upper()
            if servicios == "S":
                precio += 20
                reporte["servicios_adicionales"] += 1
            
            # Actualizar reporte
            reporte["total_boletos"] += 1
            reporte["ingresos_clase"][clase_nombre] += precio
            reporte["ingresos_tipo"][tipo_nombre] += precio
            reporte["ingresos_ruta"][ruta] = reporte["ingresos_ruta"].get(ruta, 0) + precio 
            
        total_pagar += precio

        # Proceso de pago
        print(f"\nTotal a pagar: ${total_pagar:.2f}")
        while True:
            try:
                monto = float(input("Monto recibido: $"))
                if monto >= total_pagar:
                    print(f"Vuelto: ${monto - total_pagar:.2f}")
                    break
                print("Error: Monto insuficiente.")
            except:
                print("Error: Ingrese un número válido.")
        
        input("\nPresione Enter para continuar...")

    elif opcion == "2":
        print("\n" * 50)
        print("\n--- REPORTE DEL SISTEMA ---\n")
        print(f"Total boletos vendidos: {reporte['total_boletos']}")
        print("\nIngresos por clase:")
        for clase, monto in reporte['ingresos_clase'].items():
            print(f"- {clase}: ${monto:.2f}")
        print("\nIngresos por tipo:")
        for tipo, monto in reporte['ingresos_tipo'].items():
            print(f"- {tipo}: ${monto:.2f}")
        print("\nIngresos por ruta:")
        for ruta, monto in reporte['ingresos_ruta'].items():
            print(f"- {ruta}: ${monto:.2f}")
        print(f"\nServicios adicionales solicitados: {reporte['servicios_adicionales']}")
        input("\nPresione Enter para volver al menú...")

    elif opcion == "3":
        ejecutando = False
        print("\n¡Gracias por usar LASER Airlines!")
    
    else:
        print("Opción no válida. Intente nuevamente.")
        input("Presione Enter para continuar...")