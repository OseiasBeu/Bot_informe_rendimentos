import pyautogui
import logging
import open_browser
import time
import pyperclip as pc



def GeraInforme(data):
    try:
        logging.info('--Iniciando a função Gera Informe!')
        

    except Exception as e:
        logging.error('Um erro aconteceu ao realizar o login!')
        print(e)
        logging.error(e)

if __name__ == "__main__":
    data = {
        'index': 0,
        'cpf': '000.000.000-00',
        'codigo':10101010,
        'senha': 'XXX00-00'
    }
    open_browser.OpenBrowser()
    Login(data)
