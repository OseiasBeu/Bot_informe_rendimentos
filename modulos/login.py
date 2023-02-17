import pyautogui
import logging
import open_browser
import time
import pyperclip as pc



def Login(data):
    try:
        logging.info('--Iniciando a função Login!')
        cpf = data['cpf']
        codigo = data['codigo']
        senha = data['senha']
        
        
        time.sleep(5)
        
        pyautogui.press('tab', presses=12)
        pc.copy(cpf)
        pyautogui.hotkey('ctrl', 'v')
        logging.info('CPF inserido com sucesso!')
        time.sleep(2)
        
        pyautogui.press('tab', presses=1)
        pc.copy(codigo)
        pyautogui.hotkey('ctrl', 'v')
        logging.info('Código inserido com sucesso!')
        time.sleep(2)
        
        pc.copy(senha)
        pyautogui.press('tab', presses=1)
        pyautogui.hotkey('ctrl', 'v')
        logging.info('Senha inserido com sucesso!')
        time.sleep(2)
        
        pyautogui.click('./modulos/imgs/avancar.png')
        
        
        
        logging.info('Login realizado com sucesso')
        logging.info('Finalizando a função Login!')
        return False
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
