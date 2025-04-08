import requests

def cep_valido(cep):
    # Remove caracteres especiais do CEP (ex: -, espaço)
    cep = cep.replace("-", "").replace(" ", "")
    
    # Verifica se o CEP tem 8 caracteres numéricos
    if len(cep) != 8 or not cep.isdigit():
        return False
    
    # Realiza a requisição para a API OpenCEP
    url = f"https://api.opencep.com.br/{cep}"
    response = requests.get(url)

    # Verifica se a resposta é válida
    if response.status_code == 200:
        data = response.json()
        # Verifica se o CEP retornou um resultado válido
        if "erro" not in data:
            return True
    return False

# Exemplo de uso
cep = "01001000"  # CEP de exemplo
if cep_valido(cep):
    print(f"O CEP {cep} é válido.")
else:
    print(f"O CEP {cep} não é válido.")
