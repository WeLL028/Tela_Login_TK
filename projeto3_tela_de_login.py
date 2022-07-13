# Importa tkinter

from tkinter import * # Importamos todos arquivos tkinter quando colocamos o *
from tkinter import Tk, ttk
from tkinter import messagebox

#---------Cores -----# 
cor0= '#f0f3f5' # preto
cor1= '#feffff' # branco
cor2= '#3fb5a3' # verde
cor3= '#38576b' # valor
cor4= '#403d3d' # letra

#Criando Janela 

janela=Tk()
janela.title('Login By WeLL')
janela.geometry('314x300') # largura310x300comprimento
janela.config(bg=cor1,)
janela.resizable(width=FALSE, height=FALSE)

# Dividindo a Janela 

frame_cima=Frame(janela,width=310,height=50, bg=cor1,relief='groove')
frame_cima.grid(row=0,column=0,pady=1,padx=0,sticky=NSEW)

frame_baixo=Frame(janela,width=310,height=250, bg=cor1,relief='groove')
frame_baixo.grid(row=1,column=0,pady=1,padx=0,sticky=NSEW)



# Configurando o frame cima

l_nome=Label(frame_cima, text='LOGIN', anchor=NE,font=('Ivy 25'),bg=cor1,fg=cor4)
l_nome.place(x=5,y=5)

l_linha=Label(frame_cima, text='',width=275, anchor=NW,font=('Ivy 1'),bg=cor2,fg=cor4)
l_linha.place(x=10,y=45)


# Função para verificar senha
dados = ['Welson', 'welson123']

def verificar_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login','Seja bem Vindo Admin ! ')
    elif dados[0] == nome and dados[1]==senha:
        messagebox.showinfo('Login','Seja bem Vindo de Volta ! ' +dados[0])
    else:
        messagebox.showwarning('Error','Verifique o nome e a senha !')        
        

# Configurando o frame baixo

l_nome=Label(frame_baixo, text='Nome *', anchor=NW,font=('FreeMono 10'),bg=cor1,fg=cor4)
l_nome.place(x=10,y=20)
e_nome=Entry(frame_baixo, width=25, justify='left',font=('',15),highlightthickness=1,relief='groove')
e_nome.place(x=14,y=50)


l_pass=Label(frame_baixo, text='Senha *', anchor=NW,font=('FreeMono 10'),bg=cor1,fg=cor4)
l_pass.place(x=10,y=95)
e_pass=Entry(frame_baixo, width=25, justify='left',show='*',font=('',15),highlightthickness=1,relief='groove')
e_pass.place(x=14,y=130)

b_confirmar=Button(frame_baixo,command=verificar_senha, text='Entrar',width=10,height=2,font=('Ivy 8 bold'),bg=cor2,fg=cor1,relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15,y=180)



janela.mainloop() #execução da janela