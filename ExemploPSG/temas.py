import PySimpleGUI as sg

sg.theme_previewer()

lista_de_temas = sg.theme_list()

print('Listagem de temas')
for t in lista_de_temas:
    print(t)