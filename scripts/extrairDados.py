from dados import Dados

#extraindo dados
nome_users_api = Dados('https://jsonplaceholder.typicode.com/users','','name') #instancia com a chave name
email_users_api = Dados('https://jsonplaceholder.typicode.com/users','','email') #instancia com a chave language
print(f"quantidade de nome api de usuários {nome_users_api.qtde}")
print(f"quantidade de email da api de usuários {nome_users_api.qtde}")

#processando dados
dataframe_dados_usuario = Dados.criarDataframe(nome_users_api,email_users_api) #cria um dataframe
print(dataframe_dados_usuario)
Dados.converterDateframeParaCsv(dataframe_dados_usuario,'apiUsuarios.csv') #converte data frame para csv e retorna na base 64
