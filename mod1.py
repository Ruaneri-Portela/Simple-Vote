from graphics import *
import sys
import random
import urna_sound
nome_file=""
nome_file1=""
retorno=""
c=False
####################################################
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
####################################################
def arquivo(nome_file):
    try:
     arquivo=open(file=nome_file,mode="r",encoding="UTF-8")
     global retorno
     retorno=(arquivo.readlines())
     arquivo.close
    except:
        erro("Arquivo não encontrado",1)
    return(retorno)
####################################################
def iniciar():
    win=GraphWin(title="Inicializar Urna",width=500,height=300)
    fundo=Image(Point(250,150),"bitmap12.png")
    fundo.draw(win)
    entrada=Entry(Point(250,150),25)
    entrada.draw(win)
    entrada.setFill(color_rgb(255,255,255))
    gat=True
    while gat==True:
        key=win.getKey()
        if key=="Return":
            file_name=str(entrada.getText())+".egu"
            global nome_file
            nome_file=file_name
            retorno=arquivo(file_name)
            if "---------------EGU--------------------\n" in retorno:
                 pass
            else:
                erro("Arquivo Invalido",1)
            if "---------------CFT--------------------\n" in retorno:
                 pass
            else:
                erro("Arquivo Invalido",1)
            gat=False
    win.close()
    return(file_name)
####################################################
def principal(dados):
    arquivo=arquivo_saida_criar()
    win=GraphWin(title="Urna",width=1000,height=600)
    fundo=Image(Point(500,300),"bitmap5.png")
    fundo.draw(win)
    key=None
    text1=Text(Point(195,290),"")
    text1.draw(win)
    text1.setSize(30)
    text2=Text(Point(275,290),"")
    text2.draw(win)
    text2.setSize(30)
    text3=Text(Point(355,290),"")
    text3.draw(win)
    text3.setSize(30)
    text4=Text(Point(435,290),"")
    text4.draw(win)
    text4.setSize(30)
    csg=0
    csgs=1
    cs=str(cargo_set(csg)[0])
    cs=cs.split(",")
    text5=Text(Point(200,20),"Você está votando para:"+" "+cs[0])
    text5.draw(win)
    text6=Text(Point(200,35),str(csgs)+"/"+str(len(cargo_set(csg)[1])))
    text6.draw(win)
    percuso=0
    erro=0
    gat=True
    erroAlert=Image(Point(300,40),"bitmap6.png")
    nome_candidato=Text(Point(850,100),"NOME_CANDIDATO")
    cargo=Text(Point(850,400),"CARGO")
    profile=Image(Point(850,250),"bitmap7.png")
    u=cargo_set(csg)[1]
    u1=""
    global c
    while c != True:
        if int(csgs)>int(len(cargo_set(csg)[1])):
            som(1)
            csg=0
            csgs=1
            percuso=0
        cs=str(cargo_set(percuso)[0])
        text6.setText(str(csgs)+"/"+str(len(cargo_set(csg)[1])))
        cs=cs.split(",")
        csg=0
        text5.setText("Você está votando para:"+" "+cs[0])
        erro=0
        numero_voto=""
        try:
            key=int(win.getKey())
            numero_voto=str(key)
        except:
            erroAlert.draw(win)
            win.getKey()
            erroAlert.undraw()
            erro=1
            gat=False
        if key in range (0,10) and erro==0 :
            text1.setText(key)
        try:
            key=int(win.getKey())
            numero_voto=numero_voto+str(key)
        except:
            erroAlert.draw(win)
            win.getKey()
            erroAlert.undraw()
            erro=1
            gat=False
        if key in range (0,10) and erro==0:
            text2.setText(key)
        try:
            key=int(win.getKey())
            numero_voto=numero_voto+str(key)
        except:
            erroAlert.draw(win)
            win.getKey()
            erroAlert.undraw()
            erro=1
            gat=False
        if key in range (0,10) and erro==0:
            text3.setText(key)
        try:
            key=int(win.getKey())
            numero_voto=numero_voto+str(key)
        except:
            erroAlert.draw(win)
            win.getKey()
            erroAlert.undraw()
            erro=1
            gat=False
        if key in range (0,10) and erro==0:
            text4.setText(key)
        while gat==True:
            len(u)
            u1=(u[percuso])
            u1=str(u1).split(",") 
            u2=u1[1]
            lista_up=busca_voto(numero_voto,dados,u2)
            try:
                nome_candidato.setText(lista_up[0])
                cargo.setText(lista_up[1])
                nome_candidato.draw(win)
                cargo.draw(win)
                profile.draw(win)
            except:
                pass
            key=win.getKey()
            if key == "S":
                som(2)
                csgs=csgs+1
                nome_candidato.setText("NOME_CANDIDATO")
                cargo.setText("CARGO")
                gat=False
                arquivo1=open(file=arquivo,mode="a",encoding="utf-8")
                arquivo1.write(str(lista_up[0]+","+str(int(csgs-1))+","+lista_up[1])+","+str(numero_voto)+"\n")
                arquivo1.close()
                percuso=percuso+1
                csg=int(int(csg)+1)
                reorganizar_votos()
            if key == "N":
                nome_candidato.setText("NOME_CANDIDATO")
                cargo.setText("CARGO")
                gat=False
            if key == "B":
                som(2)
                gat=False
                csgs=csgs+1
                arquivo1=open(file=arquivo,mode="a",encoding="utf-8")
                arquivo1.write(str("BRANCO"+","+str(int(csgs-1))+","+"BRANCO")+","+str("BRANCO")+"\n")
                arquivo1.close()
                csg=int(int(csg)+1)
                percuso=percuso+1
                reorganizar_votos()
        profile.undraw()
        nome_candidato.undraw()
        cargo.undraw()
        gat=True
        text1.setText("")
        text2.setText("")
        text3.setText("")
        text4.setText("")
    win.close()
####################################################
def som(a):
    if a==1:
        urna_sound.end()
    if a==2:
        urna_sound.vote_pass()
####################################################
def busca_voto(x,filename,cn):
 urna=open(file=filename,mode="r",encoding="utf-8")
 urna_data=urna.readlines()
 gat=False
 nome_uni=["Voto nulo"," "+"0"," "+cn]
 retorno=""
 retorno2=""
 for l in range (0,len(urna_data)):
     a=(urna_data[l])
     if x in a:
         p=a.strip("\n")
         nome_uni=p.split(",")
         if cn in nome_uni[2]:
          gat=True 
 if "---------------EGU--------------------\n" in urna_data:
     fim_cargos=(urna_data.index("---------------CFT--------------------\n"))
     for l in range(1,fim_cargos):
          cargo_data=urna_data[l]
          cargo_data=cargo_data.strip("\n")
          cargo_data=cargo_data.split(",")
          if gat == True:
            if nome_uni[2] in cargo_data[1]:
             return([nome_uni[0],cargo_data[0]])
     return(["Voto Nulo", "Nulo"])
 urna.close()
####################################################
def cargo_set(csg):
 global nome_file
 urna=open(file=nome_file,mode="r",encoding="utf-8")
 urna_data=urna.readlines()
 cargo_list=[]
 if "---------------EGU--------------------\n" in urna_data:
     fim_cargos=(urna_data.index("---------------CFT--------------------\n"))
     for l in range(1,fim_cargos):
          cargo_data=urna_data[l]
          cargo_data=cargo_data.strip("\n")
          cargo_data=cargo_data.split(",")
          cargo_list.append(cargo_data[0]+","+cargo_data[1])
 return(cargo_list[csg],cargo_list)
####################################################
def arquivo_saida_criar():
    a=""
    x=("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f")
    for l in range (0,9):
     a=a+str(random.choice(x))
    b="urna_"+a+".tvu"
    arquivo=open(file=b,mode="w",encoding="utf-8")
    global retorno
    u=retorno
    t=len(u)
    for l in range(0,t):
        arquivo.write(u[l])
    arquivo.write("---------------ENV--------------------\n")
    arquivo.close()
    global nome_file1
    nome_file1=b
    return(b)
####################################################
def reorganizar_votos():
    global nome_file1
    arquivo1=open(file=nome_file1,mode="r",encoding="utf-8")
    a=arquivo1.readlines()
    al=len(a)
    o=a.index("---------------ENV--------------------\n", 0)
    li=[]
    lii=[]
    for l in range(0,o):
        li.append(a[l])
    for l in range(o,al):
        lii.append(a[l])
    arquivo1.close()
    arquivo2=open(file=nome_file1,mode="w",encoding="utf-8")
    for l in range(0,len(li)):
        arquivo2.write(li[l])
    b=(sorted(lii))
    for l in range(0,len(b)):
        arquivo2.write(b[l])
    arquivo2.close()
####################################################
dados=iniciar()
principal(dados)