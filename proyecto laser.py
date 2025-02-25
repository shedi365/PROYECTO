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