import requests
import pasta_api
api_key = pasta_api.api_key
link_dado = input('Digite aqui o link para encurtar: ')
api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={link_dado}"
data = requests.get(api_url).json()['url']
if data['status'] == 7:
    link_encurtado = data['shortLink']
    print(f'Aqui está seu Link encurtado: {link_encurtado}')
else:
    print('Houve um erro', data)