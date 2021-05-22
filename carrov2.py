from colorama import init
from colorama.ansi import Fore
init()
import time
class Carro:
    def __init__(self, temperatura, nivel_oleo, bateria):
        self.temperatura = temperatura
        self.nivel_oleo = nivel_oleo
        self.bateria = bateria

    def Ligar(self):
        from colorama import Fore, Back, Style
        print(Fore.RED + 'A ligar o carro...')
        time.sleep(2)
        print(Fore.GREEN + 'Brummm')

    def Informacoes(self):
        time.sleep(1)
        print(Fore.MAGENTA + 'Temperatura = ' + self.temperatura)
        print(Fore.MAGENTA + 'Nível do óleo = ' + self.nivel_oleo)
        print(Fore.MAGENTA +'Bateria = ' + self.bateria)

    def Desligar(self):
        time.sleep(2)
        print(Fore.RED +'Carro a desligar..')

carro1 = Carro(Fore.BLUE + input('Qual a temperatura do seu carro?'), Fore.BLUE + input('Qual o nível do óleo do seu carro?'), Fore.BLUE + input('Qual a percentagem de bateria do seu carro?'))

carro1.Ligar()
carro1.Informacoes()
carro1.Desligar()


