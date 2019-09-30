#Criar um programa que:
#1. Cadastre usuário e senha.
#2. Liste usuários cadastrados e suas respectivas senhas.
#3. Efetue login, validando usuário e senha.

print('='*127)

salario = float(input('{}Digite o salario liquido: '.format( ' '*5)))

print('{}O salario liquido é:{}R${:8.2f}'.format(' '*5, ' '*9, salario))
print('{}Gasto E:{}R${:8.2f}'.format(' '*5, ' '*21, salario*0.5))
print('{}Investimentos LP:{}R${:8.2f}'.format(' '*5, ' '*12, salario*0.2))
print('{}Investimentos CP:{}R${:8.2f}'.format(' '*5, ' '*12, salario*0.1))
print('{}Livre:{}R${:8.2f}'.format(' '*5, ' '*23, salario*0.2))

print('='*127)