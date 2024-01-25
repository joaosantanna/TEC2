'''
programa para calculo de raizes de equacao do 2 grau
autor : joao
'''

import PySimpleGUI as sg
from equacao2g import equacao2g
import sys

sg.theme('DarkAmber')
desenho = [
    [sg.Text('Calculo para equacao do 2 grau')],
    [sg.Text('A:'), sg.Input(key='a')],
    [sg.Text('B:'), sg.Input(key='b')],
    [sg.Text('C:'), sg.Input(key='c')],
    [sg.Text('X1 =', key='x1')],
    [sg.Text('X2 =', key='x2')],
    [sg.Button('Calcular'), sg.Button('Sair'), sg.Button('Limpar')]
]

janela = sg.Window('Equacao 2 grau', font=('Helvetica', 12), size=(400, 250))
janela.Layout(desenho)
while True:
    evento, valores = janela.Read() # evento pega os botoes pressionados e outros eventos
    # que podem ocorrer no programa

    if evento == 'Calcular':
        a = float(valores['a'])
        b = float(valores['b'])
        c = float(valores['c'])
        r = equacao2g(a, b, c)
        if r is not False:
            janela['x1'].update(f'X1 = {r[0]:.4f}')
            janela['x2'].update(f'X2 = {r[1]:.4f}')
        else:
            janela['x1'].update('Nao exitem raizes reais')
            janela['x2'].update('')

    if evento == 'Sair' or evento == sg.WIN_CLOSED:
        break
    if evento == 'Limpar':
        janela['a'].update('')
        janela['b'].update('')
        janela['c'].update('')
        janela['x1'].update('')
        janela['x2'].update('')

janela.close()
sys.exit(0)
