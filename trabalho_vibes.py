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

        plt.plot(freq, frf_1_andar)
        plt.xlabel('Frequência [Hz]')
        plt.ylabel('Módulo da FRF no primeiro andar')
        plt.title('FRF1 Experimental')
        plt.grid()
        plt.yscale('log')
        plt.savefig("D:\\UFSC\\Vibes\\Cordioli\\Trabalho\\Grupo 6\\FRF1_andar.png")
        plt.show()

        # Plotar gráfico da FRF do segundo andar
        frf_2_andar = np.abs(df['Signal 3 (Imag.)']) + np.abs(df['Signal 3 (Real)']) # Obtém-se o módulo da FRF

        plt.plot(freq, frf_2_andar)
        plt.xlabel('Frequência [Hz]')
        plt.ylabel('Módulo da FRF no segundo andar')
        plt.title('FRF2 Experimental')
        plt.grid()
        plt.yscale('log')
        plt.savefig("D:\\UFSC\\Vibes\\Cordioli\\Trabalho\\Grupo 6\\FRF2_andar.png")
        plt.show()

        # Plotar gráfico da FRF do terceiro andar
        frf_3_andar = np.abs(df['Signal 4 (Imag.)']) + np.abs(df['Signal 4 (Real)']) # Obtém-se o módulo da FRF

        plt.plot(freq, frf_3_andar)
        plt.xlabel('Frequência [Hz]')
        plt.ylabel('Módulo da FRF no terceiro andar')
        plt.title('FRF3 Experimental')
        plt.grid()
        plt.yscale('log')
        plt.savefig("D:\\UFSC\\Vibes\\Cordioli\\Trabalho\\Grupo 6\\FRF3_andar.png")
        plt.show()

if __name__ == '__main__':
    daniel = Vibes()
    daniel.plotar_frf_excel()