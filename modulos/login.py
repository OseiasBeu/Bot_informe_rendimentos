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
        site = 'https://cav.receita.fazenda.gov.br/autenticacao/login'
        
        time.sleep(3)
        pc.copy(site)
        pyautogui.hotkey('ctrl', 'shift','n')
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'v')       
        
        pyautogui.hotkey('enter')   
        
        time.sleep(5)
        inputCpf = pyautogui.locateCenterOnScreen('./modulos/imgs/inputCPF.png', confidence = 0.8)
        pc.copy(cpf)
        time.sleep(2)
        pyautogui.click(inputCpf)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        logging.info('CPF inserido com sucesso!')
        time.sleep(2)
        
        pyautogui.press('tab', presses=1)
        pc.copy(codigo)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        logging.info('Código inserido com sucesso!')
        time.sleep(2)
        
        pc.copy(senha)
        pyautogui.press('tab', presses=1)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        logging.info('Senha inserido com sucesso!')
        time.sleep(2)
        
        avancar_btn = pyautogui.locateCenterOnScreen('./modulos/imgs/avancar.png', confidence = 0.8)
        time.sleep(2)
        pyautogui.click(avancar_btn)
        time.sleep(2)
        
        erro = pyautogui.locateCenterOnScreen('./modulos/imgs/erro.png')
        erroBloqueio = pyautogui.locateCenterOnScreen('./modulos/imgs/erroTempo.png')
        erroCNPJ = pyautogui.locateCenterOnScreen('./modulos/imgs/erroCNPJ.png')
        erroGeneric = pyautogui.locateCenterOnScreen('./modulos/imgs/erro_.png')

        time.sleep(2)
        if erro:
            logging.warn('Dados de login inválidos')
            logging.info('Finalizando a função Login!')
            return '1'
        elif erroCNPJ:
            logging.warn('Dados de login inválidos')
            logging.info('Finalizando a função Login!')
            return '1'
        elif erroBloqueio:
            logging.warn('Bloqueio temporário de tentativas')
            logging.info('Finalizando a função Login!')
            return '2'   
        elif erroGeneric:
            logging.warn('Erro no login!')
            logging.info('Finalizando a função Login!')
            return '1'  
        else:
            logging.warn('Login Realizado com sucesso')
            logging.info('Finalizando a função Login!')
            return '3'

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
