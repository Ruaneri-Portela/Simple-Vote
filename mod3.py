from os import close
from tkinter.constants import W
from graphics import *
from tkinter.filedialog import askopenfile
from openpyxl import Workbook
import creditos
global file1
file1=""
file2=""
arquivo_excel = Workbook()
planilha1 = arquivo_excel.active
planilha1.title = "Votos"
lista=[]
def maisvotos():
    global file1
    erro1=False
    listar=[]
    file2=abrir()  
    a=open(file=file2,mode="r",encoding="utf-8")
    file3=a.readlines()
    a.close
    ini2=file1.index("---------------ENV--------------------\n")
    ini=file3.index("---------------ENV--------------------\n")
    for l in range (0,ini2):
        if file1[l] in file3[l]:
            pass
        else:
            erro1=True
    if erro1 == False:
        for l in range(ini,len(file3)):
            listar.append(file3[l])
        return(listar)
    if erro1 == True:
        pp="Arquivo de votação não\nCorresponde ao usado inicialmente."
        erro(pp,1)
        return([])
def erro(causa,exitcode):
    win=GraphWin(title="Erro",width=300,height=150)
    key=None
    fundo=Image(Point(150,75),"bitmap9.png")
    fundo.draw(win)
    Causa_text=Text(Point(150,85),causa)
    Causa_text.setTextColor(color_rgb(255,0,0))
    Causa_text.draw(win)
    while key != "Escape":
        key=win.getKey()
    win.close()
    if exitcode==1:
        sys.exit()
    else:
        win.close()
def principal():
    global file1, file2
    cont=0   
    win=GraphWin(title="Contador",width=600,height=400)
    texto1=Text(Point(130,90),str(str(cont)+" "+"Arquivos de urna Contados"))
    texto2=Text(Point(300,200),str("Aperte 'Enter' para adicionar mais um arquivo.\nAperte 'Escape' para sair."))
    back=Image(Point(300,200),"bitmap13.png")
    back.draw(win)
    key=None  
    alert=Image(Point(160,35),"bitmap15.png")
    alert2=Image(Point(160,35),"bitmap16.png")
    back1=Image(Point(300,200),"bitmap14.png")
    back3=Image(Point(300,200),"bitmap17.png")
    texto1.draw(win)
    back1.draw(win)
    key=win.getKey()
    print(key)
    if key=="F1":
        creditos.creditos()
        sys.exit()
    back3.draw(win)
    back1.undraw()
    file2=abrir()  
    a=open(file=file2,mode="r",encoding="utf-8")
    file1=a.readlines()
    a.close()
    back3.undraw()
    alert.draw(win)
    cont=cont+1
    texto2.draw(win)
    while key != "Escape":
        texto1.setText(str(str(cont)+" "+"Arquivos de urna Contados"))
        key=win.getKey()
        try:
            alert2.undraw()
        except:
            pass
        try:
         alert.undraw()
        except:
            pass
        if key=="Return":
            back3.draw(win)
            r=maisvotos()
            file1=file1+r
            back3.undraw()
            try:
             if r != []:
              cont=cont+1
              alert.draw(win)  
             else:
              alert2.draw(win)
            except:
             pass  
    contagem()  
    back5=Image(Point(300,200),"bitmap18.png")  
    back5.draw(win)
    win.getKey() 
    win.close()
    saida()
def abrir():
    files = [('Tabela de Urna', '*.tvu*'),
             ('Todos os Arquivos', '*.')]
    file = askopenfile(filetypes = files, defaultextension = files)
    file=str(file).split("'")
    return(file[1])
def contagem():
    global lista
    global file1, lista
    file1=file1+addvotovazio()
    rdp=remove_repetidos(file1)
    ini=file1.index("---------------ENV--------------------\n")
    ini2=rdp.index("---------------ENV--------------------\n")
    lista_p_c=[file1]
    for l in range(ini,len(file1)):
        lista_p_c.append(file1[l])
    for l in range(ini2+1,len(rdp)):
        u=str(rdp[l])
        u=u.split(",")
        u1=(u[1])
        nome_p=""
        for l2 in range(1,file1.index("---------------CFT--------------------\n")):
            u8=file1[l2]
            u8=u8.split(",")
            if str(u1) in u8[1]:
                nome_p=u8[0]
        p8=(nome_p),(int(file1.count(rdp[l])-1)),(u[0]),(u[3])
        p8=(p8)        
        lista.append(p8)
def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l
def saida():
    global lista, planilha1,arquivo_excel
    lista.sort()
    lista2=[]
    cabe=("Cargo:","Votos:","Nome Candidato(a):","Nuemro:")
    lista2.append(cabe)
    lista2=lista2+lista
    for linha in lista2:
     planilha1.append(linha)
    arquivo_excel.save("Votos.xlsx")
def addvotovazio():
    global file1
    listaVz=[]
    listaVz2=[]
    listaR=[]
    s=""
    ini=file1.index("---------------CFT--------------------\n")
    ini2=file1.index("---------------ENV--------------------\n")
    for l in range (ini+1,ini2):
         listaVz.append(file1[l])
    ini=file1.index("---------------EGU--------------------\n")
    ini2=file1.index("---------------CFT--------------------\n")
    for l in range (ini+1,ini2):
         listaVz2.append(file1[l])
    print(1,listaVz,listaVz2)
    for l in range (0,len(listaVz)):
        s=""
        o=str(listaVz[l])
        o=o.replace("\n","")
        o=o.replace(" ","")
        o=o.split(",")
        s=s+o[0]+","+o[2]+","
        for l1 in range(0,len(listaVz2)):
            o1=str(listaVz2[l1])
            o1=o1.replace("\n","")
            o1=o1.replace(" ","")
            o1=o1.split(",")
            if o[2] in o1[1]:
                s=s+o1[0]+","
        s=s+o[1]+"\n"
        listaR.append(s)
    ini=file1.index("---------------ENV--------------------\n")
    ini2=len(file1)
    for l in range (ini+1,ini2):
         listaR.append(file1[l])
    listaR=remove_repetidos(listaR)
    return(listaR)        
principal()