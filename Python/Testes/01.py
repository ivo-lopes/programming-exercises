import PySimpleGUI as sg

## Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha  '), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]

confirm = [
    [sg.Text('Acesso liberado!')]
    [sg.Button('OK')]
]
## Janela
janela = sg.Window('Tela de Login', layout)
janela2 = sg.Window('Acesso Liberado', confirm)
## Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'ivonaldo' and valores['senha'] == 'ivonaldo123':
            confirmar = janela2.read()
            if confirmar == 'OK':
                break


