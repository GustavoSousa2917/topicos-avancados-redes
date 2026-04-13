import yaml

print("Iniciando a Parte 1 - Execução do Script")

try:
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    print(f"Aplicação: {config['app_name']}")
    print(f"Ambiente: {config['ambiente']}")
except FileNotFoundError:
    print("Arquivo config.yaml não encontrado.")