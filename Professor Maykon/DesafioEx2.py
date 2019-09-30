# Criar um programa que utilize o método 50-20-10-20:
#1. Leia o salário líquido informado pelo usuário.
#2. Organize os valores de acordo com o método citado.
#3. Informe ao usuário qual o valor que ele deve destinar para cada categoria.
print('='*127)

salario = float(input('{}Digite o salario liquido: '.format( ' '*5)))

print('{}O salario liquido é:{}R${:8.2f}'.format(' '*5, ' '*9, salario))
print('{}Gasto E:{}R${:8.2f}'.format(' '*5, ' '*21, salario*0.5))
print('{}Investimentos LP:{}R${:8.2f}'.format(' '*5, ' '*12, salario*0.2))
print('{}Investimentos CP:{}R${:8.2f}'.format(' '*5, ' '*12, salario*0.1))
print('{}Livre:{}R${:8.2f}'.format(' '*5, ' '*23, salario*0.2))

print('='*127)