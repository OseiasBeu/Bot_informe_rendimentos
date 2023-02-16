import sys,logging, schedule
sys.path.append('modulos')
from read_file import ReadFile
from open_browser import OpenBrowser


LOG_FILENAME = 'logs\log.log'
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(handlers=[logging.FileHandler(filename=LOG_FILENAME, encoding='utf-8', mode='w+')],format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
def job():
    try:
        logging.info('==========| INICIANDO BPA |==========')
        df = ReadFile('Senhas.csv')
        OpenBrowser()
        
        
        logging.info('==========| FINALIZANDO BPA |==========')
    except Exception as e:
        logging.error('==========| ERRO |==========')
        logging.error(f'Um erro inesperado aconteceu: {e}')
        logging.error('==========| ERRO |==========')


if __name__ == "__main__":
    job()