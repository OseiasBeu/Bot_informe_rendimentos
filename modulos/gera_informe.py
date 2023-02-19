import pyautogui
import logging
import time
import pyperclip as pc



def GeraInforme(nome):
    try:
        logging.info('--Iniciando a função Gera Informe!')
        #Clicar no botão: Declarações e Deomonstrativos
        declaracao_btn = pyautogui.locateCenterOnScreen('./modulos/imgs/declaracao.png', confidence = 0.8)
        time.sleep(2)
        pyautogui.click(declaracao_btn)
        time.sleep(2)      

        #Clicar na opção: Consulta e Demonstrativos
        consulta_btn = pyautogui.locateCenterOnScreen('./modulos/imgs/consulta.png', confidence = 0.8)
        time.sleep(2)
        pyautogui.click(consulta_btn)
        time.sleep(2)

        #Selecionar ano: 2021
        ano_btn = pyautogui.locateCenterOnScreen('./modulos/imgs/2021.png', confidence = 0.8)
        time.sleep(2)
        pyautogui.click(ano_btn)
        time.sleep(2)
        pyautogui.hotkey('down')
        time.sleep(2)
        
        #Clicar no botão: consultar
        consultar_btn = pyautogui.locateCenterOnScreen('./modulos/imgs/consultar.png', confidence = 0.8)
        time.sleep(2)
        pyautogui.click(consultar_btn)
        time.sleep(2)
        
        #Verifica se não tem informe:
        seminforme_img = pyautogui.locateCenterOnScreen('./modulos/imgs/Tela_Quando_naotem.png', confidence = 0.8)
        if seminforme_img:
            logging.info('Não possui informe!')
            return '4'                            

        #Clicar no botão: preparar para impressão
        pyautogui.scroll(-1000)
        preparar_btn = pyautogui.locateCenterOnScreen('./modulos/imgs/preparar.png', confidence = 0.8)
        time.sleep(2)
        pyautogui.click(preparar_btn)
        time.sleep(2) 
        
        #Clicar na aba: sistema Dirf
        SistemaDirf = pyautogui.locateCenterOnScreen('./modulos/imgs/SistemaDirf.png', confidence = 0.8)
        time.sleep(2)
        pyautogui.click(SistemaDirf)
        time.sleep(2)  
        pyautogui.hotkey('win','up')
        time.sleep(2)  
        # pyautogui.scroll(-1500)
        
        #Clicar no botão: imprimir
        # imprimir_btn = pyautogui.locateCenterOnScreen('./modulos/imgs/imprimir.png', confidence = 0.8)
        time.sleep(2)
        pyautogui.hotkey('ctrl','p')
        time.sleep(2)  
        pyautogui.hotkey('enter')
        time.sleep(2)  
        
        pc.copy(nome)
        pyautogui.hotkey('ctrl','v')
        time.sleep(2)
        pyautogui.hotkey('enter')
        time.sleep(2)
        pyautogui.hotkey('ctrl','w')
        
        #Clicar no botão: Siar
        sair_btn = pyautogui.locateCenterOnScreen('./modulos/imgs/Sair.png', confidence = 0.8)
        time.sleep(2)
        pyautogui.click(sair_btn)
        time.sleep(2)  
        pyautogui.hotkey('ctrl','w')
        
        return '0'

        
        
    except Exception as e:
        logging.error('Um erro aconteceu no processo de geração do informe de rendimentos')
        print(e)
        logging.error(e)

if __name__ == "__main__":
    time.sleep(5)
    GeraInforme('Teste')
    
