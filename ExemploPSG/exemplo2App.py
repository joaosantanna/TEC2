'''
programa para calculo de raizes de equacao do 2 grau
autor : joao
'''

import PySimpleGUI as sg
from equacao2g import equacao2g

desenho =[
    [sg.Text('Calculo para equacao do 2 grau')],
    [sg.Text('A:'), sg.Input(key='a')],
    [sg.Text('B:'), sg.Input(key='b')],
    [sg.Text('C:'), sg.Input(key='c')],
    [sg.Text('X1 =', key='x1') ],
    [sg.Text('X2 =', key='x2')],
    [sg.Button('Calcular'), sg.Button('Sair'), sg.Button('Limpar')]
]

janela = sg.Window('Equacao 2 grau', font=('Courier New',12),size=(400,250))
janela.Layout(desenho)
while True:
    botao, valores = janela.Read()
    if botao=='Calcular':
        a =float(valores['a'])
        b = float(valores['b'])
        c = float(valores['c'])
        r = equacao2g(a, b, c)
        if r != False:
            janela['x1'].update(f'X1 = {r[0]:.4f}')
            janela['x2'].update(f'X2 = {r[1]:.4f}')
        else:
            janela['x1'].update('Nao exitem raizes reais')
            janela['x2'].update('')

    if botao=='Sair':
        break
    if botao == 'Limpar':
        janela['a'].update('')
        janela['b'].update('')
        janela['c'].update('')
        janela['x1'].update('')
        janela['x2'].update('')

janela.close()