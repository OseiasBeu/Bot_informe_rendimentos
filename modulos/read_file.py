import pandas as pd
import logging


def ReadFile(path):
    try:
        logging.info('--Iniciando a função ReadFile!')
        wb = pd.read_csv(path, sep=';')
        df = pd.DataFrame(wb)
        logging.info('Arquivo carregado com sucesso')
        logging.info('Finalizando a função ReadFile!')
        return df
    except Exception as e:
        logging.error('Um erro aconteceu na leitura do arquivo!')
        logging.error(e)

if __name__ == "__main__":
    path = '../Senhas.csv'
    ReadFile(path)
