import requests
import secrets
import datetime

csrf_token = secrets.token_hex(32)
print(f"Token CSRF gerado: {csrf_token}")
# url = 'https://imeiapi.org/'
url = 'https://sigop.segup.pa.gov.br/resultado/'

dados = {
    'username': '05054994000142',
    'password': 'T&st&PmP@',
    'imei': '03172988',
    'csrf_token':csrf_token,
    'cpf':'-',
    'matricula':'-',
    'data_requisicao':datetime.datetime.today(),
}

resposta = requests.post(url, data=dados)
print(resposta.text)


# import requests

# def get_imei_info(imei):
#     # Consulta o IMEI.info
#     url = f"https://www.imei.info/pt/?imei={imei}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         # Analisa a página para obter as informações relevantes (marca e modelo)
#         # Você pode usar BeautifulSoup ou regex para extrair os dados específicos
#         # Exemplo simplificado:
#         info = response.text
#         marca = info.split("Marca:")[1].split("<")[0].strip()
#         modelo = info.split("Modelo:")[1].split("<")[0].strip()
#         return marca, modelo
#     else:
#         return None, None

# # Exemplo de uso
# imei_digitado = "350845555897085"  # Substitua pelo IMEI desejado
# marca, modelo = get_imei_info(imei_digitado)
# if marca and modelo:
#     print(f"Marca: {marca}")
#     print(f"Modelo: {modelo}")
# else:
#     print("Não foi possível obter informações para o IMEI fornecido.")
