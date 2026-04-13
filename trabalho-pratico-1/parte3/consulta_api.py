import requests

# Exemplo de consulta caso o NetBox estivesse rodando localmente no docker
NETBOX_URL = "http://localhost:8000/api/"
TOKEN = "SEU_TOKEN_AQUI"
HEADERS = {
    "Authorization": f"Token {TOKEN}",
    "Accept": "application/json"
}

print("Consultando dispositivos no NetBox...")
try:
    response = requests.get(f"{NETBOX_URL}dcim/devices/", headers=HEADERS, timeout=5)
    if response.status_code == 200:
        devices = response.json().get('results', [])
        for dev in devices:
            print(f"- Roteador: {dev['name']}")
    else:
        print("API do NetBox não alcançável (Isso é normal se o serviço não estiver rodando).")
except Exception as e:
    print(f"Erro na conexão com a API: {e}")