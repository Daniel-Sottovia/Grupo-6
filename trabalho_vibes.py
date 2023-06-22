import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Vibes():
    def __init__(self) -> None:
        pass

    def plotar_frf_excel(self):
        df = pd.read_excel("D:\\UFSC\\Vibes\\Cordioli\\Trabalho\\Grupo 6\\FRF_easy_to_import.xlsx")

        # Importar as frequências usadas;
        freq = df['Frequencia']

        # Plotar gráfico da FRF do primeiro andar
        frf_1_andar = np.abs(df['Signal 2 (Imag.)']) + np.abs(df['Signal 2 (Real)']) # Obtém-se o módulo da FRF

        plt.plot(freq[2:], frf_1_andar[2:])
        plt.xlabel('Frequência [Hz]')
        plt.ylabel('Módulo da FRF no primeiro andar')
        plt.title('FRF1 Experimental')
        plt.grid()
        plt.yscale('log')
        plt.savefig("D:\\UFSC\\Vibes\\Cordioli\\Trabalho\\Grupo 6\\FRF1_andar.png")
        plt.show()

        # Plotar gráfico da FRF do segundo andar
        frf_2_andar = np.abs(df['Signal 3 (Imag.)']) + np.abs(df['Signal 3 (Real)']) # Obtém-se o módulo da FRF

        plt.plot(freq[2:], frf_2_andar[2:])
        plt.xlabel('Frequência [Hz]')
        plt.ylabel('Módulo da FRF no segundo andar')
        plt.title('FRF2 Experimental')
        plt.grid()
        plt.yscale('log')
        plt.savefig("D:\\UFSC\\Vibes\\Cordioli\\Trabalho\\Grupo 6\\FRF2_andar.png")
        plt.show()

        # Plotar gráfico da FRF do terceiro andar
        frf_3_andar = np.abs(df['Signal 4 (Imag.)']) + np.abs(df['Signal 4 (Real)']) # Obtém-se o módulo da FRF

        plt.plot(freq[2:], frf_3_andar[2:])
        plt.xlabel('Frequência [Hz]')
        plt.ylabel('Módulo da FRF no terceiro andar')
        plt.title('FRF3 Experimental')
        plt.grid()
        plt.yscale('log')
        plt.savefig("D:\\UFSC\\Vibes\\Cordioli\\Trabalho\\Grupo 6\\FRF3_andar.png")
        plt.show()

    def obter_qsi_cada_andar(self):
        df = pd.read_excel("D:\\UFSC\\Vibes\\Cordioli\\Trabalho\\Grupo 6\\FRF_easy_to_import.xlsx")

        # Importar as frequências usadas;
        freq = df['Frequencia']

        # Plotar gráfico da FRF do primeiro andar
        frf_1_andar = np.abs(df['Signal 2 (Imag.)']) + np.abs(df['Signal 2 (Real)']) # Obtém-se o módulo da FRF

        # Vamos obter as frequências naturais e o módulo da FRF de cada pico do primeiro andar
        w_n = []
        mod_FRF = []

        # Primeiro pico
        maior = frf_1_andar[2]
        cont = 0
        for i in range(2, 50):
            if frf_1_andar[i] > maior:
                maior = frf_1_andar[i]
                cont = i

        mod_FRF.append(maior)
        w_n.append(freq[cont])

        # Segundo pico
        maior = frf_1_andar[50]
        cont = 0
        for i in range(50, 200):
            if frf_1_andar[i] > maior:
                maior = frf_1_andar[i]
                cont = i

        mod_FRF.append(maior)
        w_n.append(freq[cont])

        # Terceiro pico
        maior = frf_1_andar[50]
        cont = 0
        for i in range(200, len(frf_1_andar)):
            if frf_1_andar[i] > maior:
                maior = frf_1_andar[i]
                cont = i

        mod_FRF.append(maior)
        w_n.append(freq[cont])

        print('Primeiro Andar')
        print(f'Frequência em Hz: {w_n}')
        print(f'Módulo da FRF: {mod_FRF}')

        # Para descobrir os valores da meia banda
        meia_banda = []
        for i in range(0, len(mod_FRF)):
            meia_banda.append(mod_FRF[i]/np.sqrt(2))

        print(f'Banda de Meia-Potência {meia_banda}')

        # Agora para achar os pontos para realizar o processo de Meia Banda de Potência

        # Plotar gráfico da FRF do Segundo andar
        frf_2_andar = np.abs(df['Signal 3 (Imag.)']) + np.abs(df['Signal 3 (Real)'])

        # Vamos obter as frequências naturais e o módulo da FRF de cada pico do Segundo andar
        w_n = []
        mod_FRF = []

        # Primeiro pico
        maior = frf_2_andar[2]
        cont = 0
        for i in range(2, 50):
            if frf_2_andar[i] > maior:
                maior = frf_2_andar[i]
                cont = i

        mod_FRF.append(maior)
        w_n.append(freq[cont])

        # Segundo pico
        maior = frf_2_andar[50]
        cont = 0
        for i in range(50, 200):
            if frf_2_andar[i] > maior:
                maior = frf_2_andar[i]
                cont = i

        mod_FRF.append(maior)
        w_n.append(freq[cont])

        # Terceiro pico
        maior = frf_2_andar[50]
        cont = 0
        for i in range(200, len(frf_2_andar)):
            if frf_2_andar[i] > maior:
                maior = frf_2_andar[i]
                cont = i

        mod_FRF.append(maior)
        w_n.append(freq[cont])

        print('Segundo Andar')
        print(f'Frequência em Hz: {w_n}')
        print(f'Módulo da FRF: {mod_FRF}')

        # Para descobrir os valores da meia banda
        meia_banda = []
        for i in range(0, len(mod_FRF)):
            meia_banda.append(mod_FRF[i]/np.sqrt(2))

        print(f'Banda de Meia-Potência {meia_banda}')

        # Plotar gráfico da FRF do Terceiro andar
        frf_3_andar = np.abs(df['Signal 4 (Imag.)']) + np.abs(df['Signal 4 (Real)'])

        # Vamos obter as frequências naturais e o módulo da FRF de cada pico do Terceiro andar
        w_n = []
        mod_FRF = []

        # Primeiro pico
        maior = frf_3_andar[2]
        cont = 0
        for i in range(2, 50):
            if frf_3_andar[i] > maior:
                maior = frf_3_andar[i]
                cont = i

        mod_FRF.append(maior)
        w_n.append(freq[cont])

        # Segundo pico
        maior = frf_3_andar[50]
        cont = 0
        for i in range(50, 200):
            if frf_3_andar[i] > maior:
                maior = frf_3_andar[i]
                cont = i

        mod_FRF.append(maior)
        w_n.append(freq[cont])

        # Terceiro pico
        maior = frf_3_andar[50]
        cont = 0
        for i in range(200, len(frf_3_andar)):
            if frf_3_andar[i] > maior:
                maior = frf_3_andar[i]
                cont = i

        mod_FRF.append(maior)
        w_n.append(freq[cont])

        print('Terceiro Andar')
        print(f'Frequência em Hz: {w_n}')
        print(f'Módulo da FRF: {mod_FRF}')

        # Para descobrir os valores da meia banda
        meia_banda = []
        for i in range(0, len(mod_FRF)):
            meia_banda.append(mod_FRF[i]/np.sqrt(2))

        print(f'Banda de Meia-Potência {meia_banda}')


    def interpolacao(self, x, y):
        # No caso x e y são um array de tamanho 1 x 3
        # No caso x[0] < x[1] < x[2]

        xa = ((x[2] - x[0])*(y[1] - y[0])/(y[2] - y[0])) + x[0]

        return xa

        








if __name__ == '__main__':
    daniel = Vibes()
    #daniel.plotar_frf_excel()
    daniel.obter_qsi_cada_andar()

    '''df = pd.read_excel("D:\\UFSC\\Vibes\\Cordioli\\Trabalho\\Grupo 6\\FRF_easy_to_import.xlsx")
    frf_1_andar = np.abs(df['Signal 2 (Imag.)']) + np.abs(df['Signal 2 (Real)']) 
    freq = df['Frequencia']
    print(frf_1_andar)'''
