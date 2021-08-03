from investpy import *
import pandas as pd
from tkinter import *
from tkinter import ttk

def pegar_dolar():
    search_result = get_currency_cross_recent_data("USD/BRL",order='descending')
    result = search_result['Close'][0]
    result = result+result*0.011
    result = result+result*0.035
    result = result+result*0.011
    texto = f'DÓLAR: R${result :.3f}'
    texto_cotacoes['text'] = texto

def pegar_euro():
    search_result = get_currency_cross_recent_data("EUR/BRL",order='descending')
    result = search_result['Close'][0]
    result = result+result*0.006
    result = result+result*0.035
    result = result+result*0.011
    texto = f'EURO: R${result :.3f}'
    texto_cotacoes['text'] = texto


janela = Tk()
janela.geometry("325x150")
janela.title('PRIME Câmbio')

janela.call('source', 'azure-dark.tcl')
ttk.Style().theme_use('azure-dark')

dolarbutton = Button(janela, text = "Dólar", command = pegar_dolar)
dolarbutton.grid(column=1,row=1,padx=20, pady=25)

eurobutton = Button(janela, text = "Euro", command = pegar_euro)
eurobutton.grid(column=3,row=1)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=2,row=2, padx=30,pady=10)

janela.mainloop()