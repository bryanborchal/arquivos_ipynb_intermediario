import json
email = input('Digite o seu email: ')
senha = input('Digite a sua senha: ')
login = {
    'email' : email,
    'senha' : senha
}
with open('login.json', 'w', encoding='utf-8') as arquivo:
    json.dump(login, arquivo, indent=4, ensure_ascii=False)
with open('login.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

email = input('Digite o seu email: ')
senha = input('Digite a sua senha: ')

if email == dados['email'] and senha == dados['senha']:
    print('Acesso liberado!')
else:
    print('Acesso negado!')