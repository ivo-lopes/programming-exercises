from email.policy import default
from datetime import datetime
hora = datetime.now().strftime('%H:%M:%S - %d/%m/%Y')


class Conta:
    def __init__(self, numero, saldo, nome, tipo, cheque_especial=1000, status=False):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = status
        self.cheque_especial = cheque_especial


    def ativar(self):
        self.status = True

    def desativar(self):
        self.status = False

    def dados(self):
        if self.status == False:
            print('=' * 40)
            print(f'Nome: {self.nome}')
            print(f'Nº da conta: {self.numero}')
            print(f'Tipo da conta: {self.tipo}')
            print(f'Status: Inativa')
            print(f'Crédito especial: R${self.cheque_especial:.2f}')
            print(f'Saldo: R${self.saldo:.2f}')
            print('=' * 40)
        else:
            print('=' * 40)
            print(f'Nome: {self.nome}')
            print(f'Nº da conta: {self.numero}')
            print(f'Tipo da conta: {self.tipo}')
            print(f'Status: Ativa')
            print(f'Crédito especial: R${self.cheque_especial:.2f}')
            print(f'Saldo: R${self.saldo:.2f}')
            print('=' * 40)

    def depositar(self):
        if self.status == False:
            print('Conta inativa. Não é possível proceder com a operação.')
        else:
            deposito = float(input('Digite o valor para depósito: R$'))
            if self.cheque_especial == 1000:
                self.saldo += deposito
            else:
                self.cheque_especial = self.cheque_especial + deposito
                self.saldo += deposito
                if self.cheque_especial > 1000:
                    self.cheque_especial = 1000
            print(f'Operação realizada às {hora}')
            print('=' * 40)



    def sacar(self):
        if self.status == False:
            print('Conta inativa. Não é possível proceder com a operação.')
        else:
            saque = float(input('Digite o valor para sacar: R$'))
            if saque < self.saldo:
                self.saldo -= saque
            else:
                while saque > self.saldo:
                    print('Saldo insuficiente.')
                    continuasaque = input('Deseja proceder com o saque utilizando seu crédito de cheque especial? (S/N): ')
                    if self.saldo > 0:
                        if saque > self.cheque_especial + self.saldo:
                            print('Você não possui crédito especial suficiente para esta transação. Abortando...')
                            break
                    else:
                        if saque > self.cheque_especial:
                            print('Você não possui crédito especial suficiente para esta transação. Abortando...')
                            break
                    if continuasaque in 'YySs' and self.saldo + self.cheque_especial >= saque:
                        if self.saldo > 0:
                            self.cheque_especial = self.cheque_especial - saque + self.saldo
                            self.saldo -= saque
                            break
                        else:
                            self.cheque_especial = self.cheque_especial - saque
                            self.saldo -= saque
                            break
                    else:
                        print('Operação abortada.')
                        break
            print('=' * 40)


    def menu(self):
        while True:
            self.dados()
            print(f'0. Encerrar atividade\n'
                  f'1. Ativar conta\n'
                  f'2. Desativar conta\n'
                  f'3. Depósito\n'
                  f'4. Saque')
            menuOption = int(input('Ação: '))
            if menuOption == 0:
                print('Atividade encerrada.')
                break
            elif menuOption == 1:
                self.ativar()
                continue
            elif menuOption == 2:
                self.desativar()
                continue
            elif menuOption == 3:
                self.depositar()
                continue
            elif menuOption == 4:
                self.sacar()
                continue
            else:
                print('Ação inválida.')
                continue