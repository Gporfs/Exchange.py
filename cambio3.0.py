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
    x1= float(entry1.get())
    texto_cotacao_total['text'] = f'TOTAL: R${result*x1 :.2f}'

def pegar_euro():
    search_result = get_currency_cross_recent_data("EUR/BRL",order='descending')
    result = search_result['Close'][0]
    result = result+result*0.006
    result = result+result*0.035
    result = result+result*0.011
    texto_cotacoes['text'] = f'EURO: R${result :.3f}'
    x1= float(entry1.get())
    texto_cotacao_total['text'] = f'TOTAL: R${result*x1 :.2f}'

janela = Tk()
janela.geometry("450x250")
janela.title('PRIME Câmbio')

janela.call('source', 'azure-dark.tcl')
ttk.Style().theme_use('azure-dark')

dolarbutton = Button(janela, text = "Dólar", command = pegar_dolar)
dolarbutton.grid(column=1,row=2, padx=10)

eurobutton = Button(janela, text = "Euro", command = pegar_euro)
eurobutton.grid(column=3,row=2, padx=10)

entrada = Canvas(janela,width=300,height=100)
entrada.grid(column=2, row=1)
entry1 = Entry(janela) 
entrada.create_window(160, 50, window=entry1)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=2,row=3)

texto_cotacao_total = Label(janela, text="")
texto_cotacao_total.grid(column=2,row=4)


janela.mainloop()