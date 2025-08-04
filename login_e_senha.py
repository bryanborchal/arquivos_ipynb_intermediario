import json
email = input('Digite o seu email: ')
senha = input('Digite a sua senha: ')
login = {
    'email' : email,
    'senha' : senha
}
with open('login.json','r',encoding='utf-8') as arquivo:
    