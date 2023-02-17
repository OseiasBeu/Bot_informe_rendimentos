import sys,logging
sys.path.append('modulos')
from read_file import ReadFile
from open_browser import OpenBrowser
from login import Login
import time


LOG_FILENAME = 'logs\log.log'
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(handlers=[logging.FileHandler(filename=LOG_FILENAME, encoding='utf-8', mode='w+')],format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
def job():
    try:
        logging.info('==========| INICIANDO BPA |==========')
        df = ReadFile('Senhas.csv')
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
            Login(data)
            time.sleep(10)
        
        
        logging.info('==========| FINALIZANDO BPA |==========')
    except Exception as e:
        logging.error('==========| ERRO |==========')
        logging.error(f'Um erro inesperado aconteceu: {e}')
        logging.error('==========| ERRO |==========')


if __name__ == "__main__":
    job()