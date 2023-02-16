import pyautogui
import logging


def Login():
    try:
        logging.info('--Iniciando a função Login!')
        
        logging.info('Arquivo carregado com sucesso')
        logging.info('Finalizando a função Login!')
        return True
    except Exception as e:
        logging.error('Um erro aconteceu ao realizar o login!')
        logging.error(e)

if __name__ == "__main__":
    Login()
