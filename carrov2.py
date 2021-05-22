import time
class Carro:
    def __init__(self, temperatura, nivel_oleo, bateria):
        self.temperatura = temperatura
        self.nivel_oleo = nivel_oleo
        self.bateria = bateria

    def Ligar(self):
        print('A ligar o carro...')
        time.sleep(2)
        print('Brummm')

    def Informacoes(self):
        time.sleep(1)
        print('Temperatura = ' + self.temperatura)
        print('Nível do óleo = ' + self.nivel_oleo)
        print('Bateria = ' + self.bateria)

    def Desligar(self):
        time.sleep(2)
        print('Carro a desligar..')

carro1 = Carro(input('Qual a temperatura do seu carro?'), input('Qual o nível do óleo do seu carro?'), input('Qual a percentagem de bateria do seu carro?'))

carro1.Ligar()
carro1.Informacoes()
carro1.Desligar()


