#condicao para envio de email
#cotacao do dolar abaixo de 5.20


import requests
import smtplib
import email.message

#pegar a informação 
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")

requisicao_dicionario = requisicao.json()
#selecionando os parâmetros do dicionario especifico
#format float = são números com decimais

cotacao = float(requisicao_dicionario['USDBRL']['bid'])
print(cotacao)


#enviar um aviso por email

# ---- funcao
# variavel dentro do texto coloca-se f antes do texto e '{}'  ex..{cotacao}  -


# para a funcao def funcionar, é necessário para o parâmetro para que ela puxe a informação
def enviar_email(cotacao):
        corpo_email = f"""
        <p> Dolar está abaixo de 5.20. Cotação atual: R${cotacao}</p>
        <p> Parágrafo2</p>
        """

        msg = email.message.Message()
        msg['subject'] = "Dólar está hoje abaixo de 5.20"
        msg['From']  = 'impressora@cge.rj.gov.br'
        msg['To'] = 'grodrigues@central.rj.gov.br'
        password = 'cge@123'
        msg.add_header('content-type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtps2.webmail.gov.br: 465')
        s.starttls()
        #LOGIN CREDENTIALS FOR SENDING THE MAIL
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')

#codigo padrao 
#coment - requisicao json é um dicionario method a cima 


#logica de condicao 
if  cotacao < 5.20:
        enviar_email(cotacao)

#como colocar o codigo no servidor online
# deploy - heroku