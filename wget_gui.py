from os import system
import PySimpleGUI as Pysg


layout = [
    [Pysg.Text("Link: "), Pysg.Input(key="Link")],
    [Pysg.Button(button_text= "Download"), Pysg.Button("Continue")]
]

tela = Pysg.Window('WGet GUI', layout, element_justification='c')

while True:
    eventos, valores = tela.read()
    link_download = valores["Link"]

    if eventos == "Download":
        try: system(f"wget {link_download}")

        except:
            Pysg.Popup("ERRO")


    elif eventos == "Continue":
        try: system(f"wget -c {link_download}")

        except: Pysg.Popup("ERRO")

    if eventos == Pysg.WIN_CLOSED or eventos == "Quit":
        break

