import pyautogui
import pandas as pd
from time import sleep 
site = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
senha = 'vini355'
pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write(site)
pyautogui.press('enter')
sleep(2)
pyautogui.click(817,1601)
pyautogui.write('vini@gmail.com')
pyautogui.press('tab')
pyautogui.write(senha)
pyautogui.press('enter')
pyautogui.click(1076,1443)
tabela = pd.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:    
    pyautogui.click(1007,1440)
    codigo = tabela.loc[linha,'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab') 

    marca = tabela.loc[linha,'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')      

    tipo = tabela.loc[linha,'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')     
 
    categoria = tabela.loc[linha,'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')   

    preco_unitario = tabela.loc[linha,'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')   
   
    custo = tabela.loc[linha , 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')   

    obs = tabela.loc[linha , 'obs']
    if not pd.isna(obs):
       pyautogui.write(str(tabela.loc[linha,'obs']))
         
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)   
   