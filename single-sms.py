import requests
import json

lcbsol_api_key = "adu-central"

def enviar_sms_individual(numero_telefono, mensaje):
    """
    Envía un SMS individual utilizando la API de LCB Solutions.

    Args:
        numero_telefono (str): Número de teléfono del destinatario.
        mensaje (str): Mensaje a enviar.
    """

    url = "https://sms.lcbsol.com/api/messages/dispatch"  # Reemplaza con la URL correcta de tu API
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {lcbsol_api_key}"
        # Agrega aquí tu clave de API si es necesaria
    }

    data = {
        "to": ["numero_telefono"],
        "text": "mensaje",
        "groupName": None,
        "files": None
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print("Código de estado:", response.status_code)
    print("Contenido de la respuesta:", response.text)
    print(response.text)  # Imprime la respuesta de la API para verificar

if __name__ == "__main__":
    while True:
        numero_telefono = input("Ingrese el número de teléfono (o 'salir' para terminar): ")
        if numero_telefono.lower() == "salir":
            break
        mensaje = input("Ingrese el mensaje: ")
        enviar_sms_individual(numero_telefono, mensaje)
