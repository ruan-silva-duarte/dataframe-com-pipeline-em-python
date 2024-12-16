import requests
import base64

class Repositorios:
    def __init__(self,headers):
        self.headers = headers
    
    def criarRepositorio(self,url_perfil,json):
        response = requests.post(url_perfil,json=json,headers=self.headers)
        print(f"status da solicitação para criar repositórios {response.status_code}")
        return response.status_code
    
    def codificarDadosEmBase64(path):
        with open(path,'rb') as file:
            fileContent = file.read()
            encoded_content = base64.b64encode(fileContent)
            return encoded_content
    
    def postarArquivos(self,url_perfil,path,dada):
        url_perfil += str(path)
        print(url_perfil)
        response = requests.put(url_perfil,json=dada,headers=self.headers)
        print(f"status da solicitação para postar arquivos {response.status_code}")
        return response.status_code