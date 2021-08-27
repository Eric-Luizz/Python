import pandas as pd
from twilio.rest import Client

# faça uma conta do link abaixo
# https://www.twilio.com/docs/libraries/python

# instalar esses 3
# pip install pandas
# pip install openpyxl
# pip install twilio  

# Your Account SID from twilio.com/console
account_sid = ""# coloque o numero da sua conta criada do twilio
# Your Auth Token from twilio.com/console
auth_token  = ""#coloque o TOKEN da sua conta criada do twilio
client = Client(account_sid, auth_token)

#abrir 6 arquivos de excel
lista_meses=['janeiro','fevereiro','marco','abril','maio','junho']# lista de arquivos
tabelas_vendas = pd.read_excel('janeiro.xlsx', engine='openpyxl')# coloque caminho do seu arquivo

for mes in lista_meses:
    # print (mes)
    tabelas_vendas=pd.read_excel(f'{mes}.xlsx')
    # print(tabelas_vendas)
    if (tabelas_vendas['Vendas']>=55000).any():         
         vendedor = tabelas_vendas.loc[tabelas_vendas['Vendas']>=55000,'Vendedor'].values[0]
         vendas=tabelas_vendas.loc[tabelas_vendas['Vendas']>=55000,'Vendas'].values[0]         
         print(f'No mês {mes} alguém bateu a meta. Vendedor:{vendedor},Vendas: {vendas}')   
         message = client.messages.create(
    to="",#coloque numero do seu celular
    from_="",#coloque aqui numero do twilio
    body=f'No mês {mes} alguém bateu a meta. Vendedor:{vendedor},Vendas: {vendas}')
print(message.sid)

#Para cada arquivo:

#Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> envia SMS com o nome, o mês e as vendas

#Caso não seja maior do que 55.000 não quero fazer nada

