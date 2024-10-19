import pandas as pd
import matplotlib.pyplot as plt
import time

class SIR:
    def __init__(self, dias=1000, Suscetiveis=950, Infectados=50, Retirados=0, beta=0.05, gamma=0.01):
        # Inicialização do modelo SIR
        self.dias = dias  # Número de dias para simulação
        self.Suscetiveis = Suscetiveis  # População inicial suscetível
        self.Infectados = Infectados  # População inicial infectada
        self.Retirados = Retirados  # População inicial retirada (recuperados ou falecidos)
        self.beta = beta  # Taxa de infecção (Suscetível para Infectado)
        self.gamma = gamma  # Taxa de remoção (Infectado para Retirado)
        self.total_individuos = Suscetiveis + Infectados + Retirados  # População total
        self.resultados = None  # Armazenará os resultados do modelo
        self.modelo_executado = False  # Flag para indicar se o modelo foi executado

    def executar(self):
        Suscetiveis = [self.Suscetiveis]
        Infectados = [self.Infectados]
        Retirados = [self.Retirados]


        for dia in range(1, self.dias):
            # Cálculo das transições entre estados
            S_para_I = (self.beta * Suscetiveis[-1] * Infectados[-1])/self.total_individuos
            I_para_R = Infectados[-1] * self.gamma
            
            # Atualização das populações
            Suscetiveis.append(Suscetiveis[-1] - S_para_I)
            Infectados.append(Infectados[-1] + S_para_I - I_para_R)
            Retirados.append(Retirados[-1] + I_para_R)
        
        # Criação do DataFrame com os resultados
        self.resultados = pd.DataFrame.from_dict({
            'Dia': list(range(len(Suscetiveis))),
            'Suscetiveis': Suscetiveis, 
            'Infectados': Infectados, 
            'Retirados': Retirados
        }, orient='index').transpose()
        
        self.modelo_executado = True
        # Configurar opções de exibição do pandas
        pd.set_option('display.float_format', '{:.0f}'.format)
    def plotar(self):
        # Verifica se o modelo já foi executado
        if self.modelo_executado == False:
            print('Erro: O modelo não foi executado. Por favor, chame SIR.executar()')
            return
        
        # Plota os dados para Suscetíveis (azul), Infectados (vermelho) e Retirados (verde)
        plt.plot(self.resultados['Dia'], self.resultados['Suscetiveis'], color='blue')
        plt.plot(self.resultados['Dia'], self.resultados['Infectados'], color='red')
        plt.plot(self.resultados['Dia'], self.resultados['Retirados'], color='green')
        
        # Define rótulos para os eixos
        plt.xlabel('Dia')
        plt.ylabel('População')
        
        # Adiciona uma legenda
        plt.legend(['Suscetíveis', 'Infectados', 'Retirados'], 
            prop={'size': 10}, 
            loc='upper right',  # Mudado para 'upper right'
            # Removida a linha bbox_to_anchor
            ncol=1, 
            fancybox=True, 
            shadow=True)
        
        # Define o título do gráfico com os valores de beta e gamma
        # plt.title(r'$\beta = {0}, \gamma = {1}$'.format(self.beta, self.gamma), pad=20)
    # Adiciona o título como texto na posição desejada
        plt.text(0.6, 0.5, r'$\beta = {0}, \gamma = {1}$'.format(self.beta, self.gamma),
                transform=plt.gca().transAxes, fontsize=10, verticalalignment='center')
        
        # Ajusta o layout para acomodar a legenda
        plt.tight_layout()
        # Salva o gráfico como uma imagem PNG
        timestamp = int(time.time())
        nome_arquivo = f'grafico_{timestamp}.png'
        plt.savefig(nome_arquivo)
        plt.show()
        # Fecha a figura para liberar memória
        plt.close()


# Exemplo de uso
modelo = SIR(dias = 1000, Suscetiveis = 1571, Infectados = 99, Retirados = 0, beta = 0.05, gamma = 0.01)
modelo.executar()
modelo.plotar()   