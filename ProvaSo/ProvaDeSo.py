import time
import random
from connectdb import *

print('=' * 30)
print('{:^30}'.format('Bem vindo ao Mc´Donalds'))
print('=' * 30)

i = 1

print('-' * 29)
print('|', '{:^25}'.format('1 - Big Mac: 10,90'), '|')
print('-' * 29)
print('|', '{:^25}'.format('2 - Cheddar Mcmelt: 10,90'), '|')
print('-' * 29)

while (True):
    nome = input('Qual seu nome?')
    cpf = input('Qual seu cpf?')
    escolhaLanche = input('Quais lanches você quer?')

    x = random.randint(100,300)
    umLanche = 10.90 * 1
    doisLanche = 10.90 * 2

    if(escolhaLanche == 'Big mac'):
        print('Senha do pedido', x)
        print('Nome: ', nome)
        print('CPF: ', cpf)
        print('Lanche 1: Big mac -> 10,90')
        print('Pedido finalizado: ', umLanche)
    else:
        print('Senha do pedido', x)
        print(nome)
        print(cpf)
        print('Lanche 1: Big mac -> 10,90')
        print('Lanche 2: Cheddar Mcmelt -> 10,90')
        print('Pedido finalizado: ', doisLanche)


    print('-' * 30)
    print('Obrigado pela preferência, volte sempre!')

    insert_db(numeroPedido, nome, cpf, escolhaLanche)
    
    time.sleep(2)

    i = i + i
    
    

