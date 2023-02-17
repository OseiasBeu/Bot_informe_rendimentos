import sys,logging
sys.path.append('modulos')
from read_file import ReadFile
from open_browser import OpenBrowser
from login import Login
import time
import pyautogui
import warnings
warnings.filterwarnings('ignore')


LOG_FILENAME = 'logs\log.log'
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(handlers=[logging.FileHandler(filename=LOG_FILENAME, encoding='utf-8', mode='w+')],format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
def job():
    try:
        logging.info('==========| INICIANDO BPA |==========')
        pyautogui.alert("O código vai começar. Não utilize nada do computador até o código finalizar!")
        time.sleep(3)
        df = ReadFile('Senhas.csv')
        status = {
            '0': 'Sucesso',
            '1': 'Dados de login inválidos!',
            '2': 'Bloqueio temporário de tentativas',
            '3': 'Login Realizado com sucesso!'
        }
        # print(df)
        for index, row in df.iterrows():
            data = {
                'index': index,
                'cpf': row['cpf'],
                'codigo': row['codigo'],
                'senha': row['senha']
            }
            print(data)
            OpenBrowser()
            status_login = Login(data)
            print(status_login)
            if status_login == '1':
                df['FEITO'][index] = status['1']
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'w')
                
                
            elif status_login == '2':
                df['FEITO'][index] = status['2']
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'w')
                
            else:
                df['FEITO'][index] = status['3']
                break
                
            
            print(df)
            # break
        
        
        logging.info('==========| FINALIZANDO BPA |==========')
    except Exception as e:
        logging.error('==========| ERRO |==========')
        logging.error(f'Um erro inesperado aconteceu: {e}')
        logging.error('==========| ERRO |==========')


if __name__ == "__main__":
    job()