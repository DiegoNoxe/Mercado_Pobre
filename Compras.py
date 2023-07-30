comprador = 10
compras_feitas = []
def titulo():
    print()
    print('''\033[1;31m                     Simulador de supermercado pobre 1.0\033[m''')
    print()
def produtos():
    print()
    print('''\033[1;30m                    Temos os seguintes produtos disponiveis:
    
                    \033[1;34mCoca-cola 2l    > 7RS     (1)
                    Guaravita 150ml > 1RS     (2)
                    Caderno grande  > 3RS     (3)

OU APERTE (4) PARA SAIR DO MERCADO E ENCERRA O PROGRAMA.

Em breve mais produtos serão adicionados!\033[m''')
    print()
def total():
 global compras
 print()
 try:
  compras = int(input('\033[1;36mEscolha o produto: \033[m'))
  saldo()
 except ValueError:
     print('Ops! Opção invalida! Tente novamente.')
     total()
def saldo():
    global comprador
    global compras
    if compras == 1:
        print('\033[1;32mOk, você comprou a COCA-COLA 2L! Foi retirado 7 reais do seu saldo!')
        comprador-= 7
        print('\033[1;35mSaldo: \033[m', comprador)
        compras_feitas.append('Coca-cola 2L')
    elif compras == 2:
        print('\033[1;32mOk, você comprou o Guaravita 150ml! Foi retirado 1 real do seu saldo!')
        comprador -= 1
        print('\033[1;35mSaldo: \033[m', comprador)
        compras_feitas.append('Guaravita 150ml')
    elif compras == 3:
        print('\033[1;32mOk, você comprou o Caderno grande! Foi retirado 3 reais do seu saldo!')
        print('\033[1;35mSaldo: \033[m', comprador)
        comprador -=3
        compras_feitas.append('Caderno grande')
    elif compras == 4:
        print('\033[1;32mSaindo do mercado...')
        print('\033[1;35mSaldo: \033[m', comprador)
        print('\033[1;30mCompras feitas:')
        print('\033[1;33m')
        for compra in compras_feitas:
         print('>{}<'.format(compra))
        exit()
    return False
def controle_financeiro():
    global comprador
    if   comprador == 0:
        print('''\033[1;32mOpa, aqui é o banco NOXE, vimos que você comprou um produto e ficou com saldo negativo
    infelizmente não podemos aprovar a sua compra! END GAME!\033[m''')
        print('\033[1;32mCompras feitas: ')
        for compras in compras_feitas:
            print('>{}<'.format(compras))
        exit()
    elif comprador < -1:
        print('''\033[1;32mOpa, você não tem saldo! E está devendo ao banco agora! END GAME''')
        print()
        print('\033[1;30Compras feitas: ')
        for compras in compras_feitas:
            print('>{}<'.format(compras))
        exit()
    elif comprador == 8:
        print('\033[1;30mUau! Você está movimentando a conta :O Tome 2 reais extras!\033[m')
        comprador+= 2
titulo()
produtos()
while True:
 total()
 controle_financeiro()


