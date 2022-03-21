# Simulador de Dados
#Simular o uso do dado, gerando um valor de 1  ate 6
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valormaximo = 6
# layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
    ]



    def Iniciar(self):
        # criar uma janela
        self.janela = sg.Window('Simulador de Dado', self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Agradecemos sua participação!')
            else:
                print('Please digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valormaximo))

simulador = SimuladorDeDado()
simulador.Iniciar()