import requests
import pandas as pd

class Dados:
    
    def __init__(self,url,headers,key):
        self.url = url
        self.headers = headers
        self.key = key
        self.dados = self.criarListas()
        self.qtde = len(self.dados)
    
    def criarListas(self):
        dados = []
        for page_num in range(1,7):
            try:
                url_page = self.url
                if '?' in url_page:
                    url_page += str(page_num)
                r=requests.get(url_page,headers=self.headers)
                for res in r.json():
                    dados.append(res[self.key])
            except:
                dados.append(None)
        return dados

    def criarDataframe(v1,v2):
        dados_amz = pd.DataFrame()
        dados_amz[v1.key] = v1.dados
        dados_amz[v2.key] = v2.dados
        return dados_amz
    
    def converterDateframeParaCsv(dataframe,path):
        dataframe.to_csv(path)

        
    