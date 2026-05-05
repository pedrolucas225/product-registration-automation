#bibliotecas 
import pyautogui
import time
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

pyautogui.PAUSE = 1
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
#Passo 1: Entrar no sistema da empresa
#abrir o navegador
pyautogui.press('Win')
pyautogui.write('chrome')
pyautogui.press('Enter')

pyautogui.write(link)
pyautogui.press('Enter')
#fazer uma pausa para o site carregar
time.sleep(3)
#Passo 2: Fazer login
pyautogui.click(x=787, y=372) #clicar no campo de email
pyautogui.write(os.getenv("EMAIL"))
pyautogui.press("Tab")
pyautogui.write(os.getenv("SENHA"))
pyautogui.press("Enter")
#fazer uma pausa maior para o sistema carregar
time.sleep(3)
#Passo 3: Abrir a base de dados
tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    #Passo 4: Cadastrar 1 produtos
    #clicar na Aba Código do produto
    pyautogui.click(x=775, y=257) #clicar na Aba Código do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("Tab")

    #Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("Tab")

    #Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("Tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("Tab")

    #preço
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("Tab")

    #Custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("Tab")


    #OBS 
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("Tab")
    pyautogui.press("Enter")

    pyautogui.scroll(5000)

