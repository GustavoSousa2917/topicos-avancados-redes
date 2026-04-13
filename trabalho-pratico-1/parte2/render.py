import yaml
from jinja2 import Template

# 1. Carregar as variáveis do YAML
with open('vars.yaml', 'r') as f:
    vars_dict = yaml.safe_load(f)

# 2. Carregar o template Jinja2
with open('bgp.j2', 'r') as f:
    template = Template(f.read())

# 3. Renderizar a configuração
config_renderizada = template.render(vars_dict)

# 4. Salvar o arquivo bgpd.conf
with open('bgpd.conf', 'w') as f:
    f.write(config_renderizada)

print("Arquivo bgpd.conf gerado com sucesso!")