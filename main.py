#Passo a passo do projeto

#passo 1: Abrir o navegador 
#passo 2: Entrar no sistema da empresa
#passo 3: Fazer login
#passo 4: Importar a base de produtos pra cadastrar
#passo 5: Preencher o formulário de cadastro de produtos e salvar o cadastro
#passo 6: Repetir o processo até cadastrar todos os produtos

import pyautogui as pag
import time 
import pandas as pd
link = ('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pag.PAUSE = 0.5
#Opcional desative o recurso de segurança do pyautogui
pag.FAILSAFE = True
pag.alert('Mova o mouse para o canto superior esquerdo da tela para abortar o código')
pag.alert('O código vai começar, não mexa no computador')
pag.press('win')
pag.write('microsoft edge')
pag.press('enter')
time.sleep(3)
pag.write(link)
pag.press('enter')
time.sleep(3)
pag.click(x=668, y=401)
pag.write('erickpython@hotmail.com')
pag.press('tab')
pag.write('erickpython')    
pag.press('tab')
pag.press('enter')
time.sleep(3)
pag.click(x=676, y=283)
tabela = pd.read_csv('produtos.csv')
for linha in tabela.index:
    codigo = tabela.loc[linha, 'codigo']
    pag.write(codigo)
    pag.press('tab')
    marca = tabela.loc[linha, 'marca']
    pag.write(marca)
    pag.press('tab')
    tipo = (str(tabela.loc[linha, 'tipo']))
    pag.write(tipo)
    pag.press('tab')
    categoria = (str(tabela.loc[linha, 'categoria']))
    pag.write(categoria)
    pag.press('tab')
    preco_unitario = (str(tabela.loc[linha, 'preco_unitario']))
    pag.write(preco_unitario)
    pag.press('tab')
    custo = (str(tabela.loc[linha, 'custo']))
    pag.write(custo)
    pag.press('tab')
    obs = (str(tabela.loc[linha, 'obs']))
    if obs != 'nan':    
        pag.write(obs)
    pag.press('tab')
    pag.press('enter')
    time.sleep(1)
    pag.scroll(4000)
    time.sleep(1)
    pag.click(x=676, y=283)


    






