import requests
import zoho

# Credenciales (reemplaza con tus datos)
lcbsol_api_key = "aducentral"
zoho_user = "itsupport@adu-central.com"
zoho_password = "2024Titiapps"
zoho_module = "Leads"  # Ajusta según tu módulo
zoho_fields = ["First Name", "Phone", "Message"]

# Función para obtener las respuestas de LCBSol
def get_lcbsol_responses():
    url = "https://sms.lcbsol.com/api/customer/webhook"
    headers = {"Authorization": f"Bearer {lcbsol_api_key}"}
    response = requests.get(url, headers=headers)
    return response.json()

# Función para crear un registro en Zoho
def create_zoho_record(data):
    zoho.authenticate(username=zoho_user, password=zoho_password)
    module = zoho.crm.get_module(zoho_module)
    response = module.create_records([data])
    return response

# Función principal
def main():
    responses = get_lcbsol_responses()
    for response in responses:
        # Extrae los datos relevantes de la respuesta de LCBSol
        # ...
        # Crea un diccionario con los datos para Zoho
        zoho_data = {
            "First Name": response["nombre"],
            "Phone": response["telefono"],
            "Message": response["mensaje"]
        }
        # Crea el registro en Zoho
        create_zoho_record(zoho_data)

if __name__ == "__main__":
    main()
