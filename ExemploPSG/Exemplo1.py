import PySimpleGUI as sg

desenho =[
    [sg.Text('Programa de exemplo')],
    [sg.Text('Nome:') , sg.InputText()],
    [sg.Text('Email:') , sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

janela = sg.Window('Exemplo 1',font=('Helvetica', 14), size=(400,200)).Layout(desenho)
while True:
    botao, valores = janela.Read()
    print(f'{botao} - {valores}')
    if botao == 'Submit':
        break

janela.close()

