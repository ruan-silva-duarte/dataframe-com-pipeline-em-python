from Repositorios import Repositorios

base_url ='https://api.github.com'
username = 'user'
url_perfil = f"{base_url}/user/repos" #endpoint para criar repositorios

propiedades_repositorios = {
  "name": "meu-novo-repositorio", #colocar - no lugar de space
  "description": "criando meu novo repositorio",
  "private": False
}

nome_repositorio = propiedades_repositorios['name']
path = 'api.csv'
url_perfil_path = f"{base_url}/repos/{username}/{nome_repositorio}/contents/" #perfil e repositorório em que o arquivo será postado


#headers
acess_token = "seu token"
headers = {"authorization":'Bearer ' + acess_token,
           'X-GitHub-Api-Version':'2022-11-28'
           }

#criando repositório
repositorios = Repositorios(headers)
repositorios.criarRepositorio(url_perfil,propiedades_repositorios)
dados_base64_Api_Users = Repositorios.codificarDadosEmBase64('apiUsuarios.csv')

#colocando base 64 em repositório

dados_arquivo_apiUsuarios = {
    'message':'adicionando um novo arquivo',
    'content': dados_base64_Api_Users.decode('utf-8') #arquivo csv
}

repositorios.postarArquivos(url_perfil_path,'dados-api.csv',dados_arquivo_apiUsuarios)