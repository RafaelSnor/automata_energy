import csv
from datetime import datetime, timedelta

def imprimir_csv(archivo_csv):
    with open(archivo_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

def calcular_autonomia(archivo_csv):
    tiempo_maximo_apagado = timedelta(minutes=11)  # 6 minutos
    ultima_fecha = None

    with open(archivo_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Saltar la primera fila (cabecera)
        for row in reader:
            fecha = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')

            if ultima_fecha is not None:
                tiempo_transcurrido = fecha - ultima_fecha
                if tiempo_transcurrido > tiempo_maximo_apagado:
                    return "UPS NO CUMPLIO AUTONOMIA"
            
            ultima_fecha = fecha

    return "UPS CUMPLIO AUTONOMIA"

# Función para imprimir el contenido del archivo CSV
archivo_csv = 'datos_ups.csv'
print("Contenido del archivo CSV:")
imprimir_csv(archivo_csv)

# Calcular el tiempo de autonomía de la UPS
resultado = calcular_autonomia(archivo_csv)
print("\nResultado:", resultado)
