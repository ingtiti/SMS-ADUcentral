import requests
import csv
import json

def enviar_sms_masivos(archivo_csv, mensaje):
    """
    Envía SMS masivos utilizando un archivo CSV y la API de LCB Solutions.

    Args:
        archivo_csv (str): Ruta al archivo CSV con los números de teléfono.
        mensaje (str): Mensaje a enviar.
    """

    url = "https://sms.lcbsol.com/api/messages/dispatch"  # Reemplaza con la URL correcta de tu API
    headers = {
        "Content-Type": "application/json",
        # Agrega aquí tu clave de API si es necesaria
    }

    with open(archivo_csv, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            numero_telefono = row[0]  # Asume que el número de teléfono está en la primera columna
            data = {
                "to": [numero_telefono],
                "text": mensaje,
                "groupName": None,
                "files": None
            }
            response = requests.post(url, headers=headers, data=json.dumps(data))
            print(response.text)  # Imprime la respuesta de la API para verificar

if __name__ == "__main__":
    archivo_csv = input("Ingrese la ruta del archivo CSV: ")
    mensaje = input("Ingrese el mensaje a enviar: ")
    enviar_sms_masivos(archivo_csv, mensaje)
