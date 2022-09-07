import pyautogui 
from  time import sleep
#1 - clicar e digitar meu usuario
pyautogui.click(673,387,duration=1)
pyautogui.write('papai')

pyautogui.click(672,410,duration=2)
pyautogui.write('123456')
pyautogui.click(684,443,duration=1)
pyautogui.click(609,440,duration=0.5)
'''pyautogui.click(673,387,duration=2)
pyautogui.write('papai')
#2 - clicar e digitar minha senha
pyautogui.click(672,410,duration=2)
pyautogui.write('123456')'''
#3 - clicar em entrar
pyautogui.click(603,443,duration=1)
#4 - extrair cada produto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preço = linha.split(',')[2]
        # -1 - clicar e digitar produto
        pyautogui.click(390,372,duration=0.5)
        pyautogui.write(produto)
        # -2 - clicar e digitar quantidade
        pyautogui.click(388,401,duration=0.5)
        pyautogui.write(quantidade)
        # -3 - clicar e digitar preço
        pyautogui.click(388,421,duration=0.5)
        pyautogui.write(preço)
        # -4 - clicar e registrar
        pyautogui.click(324,583,duration=0.5)
