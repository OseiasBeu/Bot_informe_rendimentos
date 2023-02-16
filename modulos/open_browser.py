import webbrowser
import logging

def OpenBrowser():
    try:
        logging.info('--Iniciando a função OpenBrowser!')
        webbrowser.open_new_tab('https://cav.receita.fazenda.gov.br/autenticacao/login')
        logging.info('Navegador aberto')
        logging.info('Finalizando a função OpenBrowser!')
    except Exception as e:
        logging.error('Um erro aconteceu na abertura do navegador!')
        logging.error(e)

if __name__ == "__main__":
    OpenBrowser()