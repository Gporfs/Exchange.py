from PySimpleGUI import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.headless = True
nav = webdriver.Chrome(options=chrome_options)
nav.get('https://br.investing.com/currencies/usd-brl')
aba_dolar = nav.window_handles[0]
dolar = nav.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]').text
nav.execute_script("$(window.open('https://br.investing.com/currencies/eur-brl'))")
aba_euro = nav.window_handles[1]
nav.switch_to.window(aba_euro)
euro = nav.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]').text
nav.switch_to.window(aba_dolar)
dolar = float(dolar.replace(',','.'))
euro = float(euro.replace(',', '.'))
dolar = dolar+dolar*0.011
dolar = dolar+dolar*0.035
dolar = dolar+dolar*0.011
euro =  euro+euro*0.006
euro = euro+euro*0.035
euro = euro+euro*0.011

sg.theme("Reddit")
layout = [
    [sg.Text(f'U$ {dolar :.2f} '), sg.Text(f'€ {euro :.2f}')],
    [sg.Text('Qual moeda?(dolar-1/euro-2)'),sg.Input(key='moeda',size=(10,1)), sg.Text('Quantidade:'), sg.Input(key='x',size=(10,1))],
    [sg.Button('Calcular'), sg.Button('Refresh')]
]

janela = sg.Window('Prime Câmbio', layout)

while True:
    eventos, valores = janela.read()
    if eventos== sg.WINDOW_CLOSED:
        break
    if eventos == 'Calcular':
        nav.switch_to.window(aba_dolar)
        dolar = nav.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]').text
        nav.switch_to.window(aba_euro)
        euro = nav.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]').text
        dolar = float(dolar.replace(',','.'))
        euro = float(euro.replace(',', '.'))
        dolar = dolar+dolar*0.011
        dolar = dolar+dolar*0.035
        dolar = dolar+dolar*0.011
        euro =  euro+euro*0.006
        euro = euro+euro*0.035
        euro = euro+euro*0.011
        if valores['moeda'] == '1':    
            sg.popup(f'U$ {float(valores["x"])*dolar :.2f}')
        elif valores['moeda'] == '2':    
            sg.popup(f'€ {float(valores["x"])*euro :.2f}')
        else:
            sg.popup('ERRO')
        if eventos == 'Refresh':
            nav.switch_to.window(aba_dolar)
            dolar = nav.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]').text
            nav.switch_to.window(aba_euro)
            euro = nav.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]').text
            dolar = float(dolar.replace(',','.'))
            euro = float(euro.replace(',', '.'))
            dolar = dolar+dolar*0.011
            dolar = dolar+dolar*0.035
            dolar = dolar+dolar*0.011
            euro =  euro+euro*0.006
            euro = euro+euro*0.035
            euro = euro+euro*0.011
            janela.hide()
            janela.refresh()
            janela.un_hide()