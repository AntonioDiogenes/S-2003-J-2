from tkinter import *
def converter_km(op,val):
    if op == Options_2[0]:
        return val
    if op == Options_2[1]:
        return int(val) * 10
    if op == Options_2[2]:
        return int(val) * 100
    if op == Options_2[3]:
        return int(val) * 1000
    if op == Options_2[4]:
        return int(val) * 10000
    if op == Options_2[5]:
        return int(val) * 100000
    if op == Options_2[6]:
        return int(val) * 1000000   
def converter_hm(op,val):
    if op == Options_2[0]:
        return int(val) / 10
    if op == Options_2[1]:
        return int(val)
    if op == Options_2[2]:
        return int(val) * 10
    if op == Options_2[3]:
        return int(val) * 100
    if op == Options_2[4]:
        return int(val) * 1000
    if op == Options_2[5]:
        return int(val) * 10000
    if op == Options_2[6]:
        return int(val) * 100000
def converter_dam(op,val):
    if op == Options_2[0]:
        return int(val) / 100
    if op == Options_2[1]:
        return int(val) /10
    if op == Options_2[2]:
        return int(val)
    if op == Options_2[3]:
        return int(val) * 10
    if op == Options_2[4]:
        return int(val) * 100
    if op == Options_2[5]:
        return int(val) * 1000
    if op == Options_2[6]:
        return int(val) * 10000
def converter_m(op,val):
    if op == Options_2[0]:
        return int(val) / 1000
    if op == Options_2[1]:
        return int(val) /100
    if op == Options_2[2]:
        return int(val) / 10
    if op == Options_2[3]:
        return int(val)
    if op == Options_2[4]:
        return int(val) * 10
    if op == Options_2[5]:
        return int(val) * 100
    if op == Options_2[6]:
        return int(val) * 1000
def converter_dm(op,val):
    if op == Options_2[0]:
        return int(val) / 10000
    if op == Options_2[1]:
        return int(val) /1000
    if op == Options_2[2]:
        return int(val) / 100
    if op == Options_2[3]:
        return int(val) / 10
    if op == Options_2[4]:
        return int(val)
    if op == Options_2[5]:
        return int(val) * 10
    if op == Options_2[6]:
        return int(val) * 100
def converter_cm(op,val):
    if op == Options_2[0]:
        return int(val) / 100000
    if op == Options_2[1]:
        return int(val) /10000
    if op == Options_2[2]:
        return int(val) / 1000
    if op == Options_2[3]:
        return int(val) / 100
    if op == Options_2[4]:
        return int(val) / 10
    if op == Options_2[5]:
        return int(val) 
    if op == Options_2[6]:
        return int(val) * 10
def converter_mm(op,val):
    if op == Options_2[0]:
        return int(val) / 1000000
    if op == Options_2[1]:
        return int(val) /100000
    if op == Options_2[2]:
        return int(val) / 10000
    if op == Options_2[3]:
        return int(val) / 1000
    if op == Options_2[4]:
        return int(val) / 100
    if op == Options_2[5]:
        return int(val) / 10
    if op == Options_2[6]:
        return int(val)

def converter(opcao_1,opcao_2,valor):
    if opcao_1 == Options_1[0]:
        label_resultado['text'] = converter_km(opcao_2,valor)
        
    if opcao_1 == Options_1[1]:
        label_resultado['text'] = converter_hm(opcao_2,valor)
        
    if opcao_1 == Options_1[2]:
        label_resultado['text'] = converter_dam(opcao_2,valor)
        
    if opcao_1 == Options_1[3]:
        label_resultado['text'] = converter_m(opcao_2,valor)
        
    if opcao_1 == Options_1[4]:
        label_resultado['text'] = converter_dm(opcao_2,valor)
        
    if opcao_1 == Options_1[5]:
        label_resultado['text'] = converter_cm(opcao_2,valor)
        
    if opcao_1 == Options_1[6]:
        label_resultado['text'] = converter_mm(opcao_2,valor)
        
def executa():
       converter(variable_1.get(),
                 variable_2.get(),
                 entry_valor.get())

main_windown = Tk()
main_windown.title('conversor')

label_titulo = Label(main_windown,text='conversor')
label_titulo.grid(column=1,row=0)

entry_valor = Entry(main_windown,width=21)
entry_valor.grid(column=0,row=1)

label_igualdade = Label(main_windown,text='=')
label_igualdade.grid(column=1,row=1)

label_resultado = Label(main_windown,text='')
label_resultado.grid(column=2,row=1)

Options_1 = ['(KM) quilometro',
           '(HM) hectometro',
           '(DAM)decametro',
           '(M)  metro',
           '(DM) decimetro',
           '(CM) centimetro',
           '(MM) milimetro']
variable_1 = StringVar(main_windown)
variable_1.set(Options_1[0])
drop_1 = OptionMenu(main_windown,variable_1,*Options_1)
drop_1.grid(column=0,row=2)

Options_2 = ['(KM) quilometro',
           '(HM) hectometro',
           '(DAM)decametro',
           '(M)  metro',
           '(DM) decimetro',
           '(CM) centimetro',
           '(MM) milimetro']
variable_2 = StringVar(main_windown)
variable_2.set(Options_2[0])
drop_2 = OptionMenu(main_windown,variable_2,*Options_2)
drop_2.grid(column=2,row=2)

button = Button(main_windown,text='converter',command=executa)
button.grid(column=1,row=2)

mainloop()
