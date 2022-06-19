from creditos import creditos
from graphics import *
import sys
#####################################################
def ajuda():
    win=GraphWin(title="Ajuda e Sobre",width=600,height=300)
    win.setBackground(color_rgb(199,0,36))
    intenal=Rectangle(Point(10,10),Point(590,290))
    intenal.setOutline(color_rgb(246,162,1))
    intenal.setFill(color_rgb(246,162,1))
    intenal.draw(win)
    ajuda_text=Text(Point(300,130),"Ajuda (Pagina 1)\nPara gerar o arquivo informe o nome na de solicitação\n\n(O arquivo sera salvo na pasta que está o programa\n(Não e aceito espaços dentro do nome do arquivo)")
    ajuda_text.draw(win)
    nav_ps=Text(Point(70,20),"Pagina => 1/3")
    nav_ps.draw(win)
    nav_text=Text(Point(300,265),"1=>Ajuda(1) =/= 2=>Ajuda(2) =/= 3=>Sobre\n Esc => Sair (!! Encerra o programa"") \n Para navegar use as setas para esquerda ou direita do teclado")
    nav_text.draw(win)
    key=None
    nav=1
    while key != "Escape":
        key=win.getKey()
        if key == "Left" and nav>1:
            nav=nav-1
        if key == "Right" and nav<3:
            nav=nav+1
        if nav == 1:
            nav_ps.setText("Pagina => 1/3")
            ajuda_text.setText("Ajuda (Pagina 1)\n'Para gerar o arquivo informe o nome na de solicitação'\n\n(O arquivo sera salvo na pasta que está o programa\n(Não e aceito espaços dentro do nome do arquivo)")
        if nav == 2:
            nav_ps.setText("Pagina => 2/3")
            ajuda_text.setText("Ajuda (Pagina 2)\n\n'Devido a  limitações do programa algumas etapas fora do\n previsto requerem reinicio da aplicação.'\n\n'Na tela informe o nome, numero e cargo que o \ncandidato está concorrendo para que\n aja a injeção na urna\n\n Quando finalizado aperte 'Esc', e 'Confirime a solicitação'")
        if nav == 3:
            nav_ps.setText("Pagina => 3/3")
            ajuda_text.setText("Sobre\n\nCriado por Ruaneri Ferreira Portela\n\n SimpleVote Modulo 3 (Programa de configuração de urna)\n\n 'Projeto modular para a a avaliação do segundo bimestre\n da materia algoritimos e estrututura de dados da\nUniversidade Federal do Rio Grande'\n\n Setembro de 2021/Versão 1.0")
    win.close()
    creditos()
    sys.exit()
#####################################################
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
def arquivo_saida():
    win=GraphWin(title="Defina o nome do arquivo de saida:",width=400,height=200)
    key=None
    fundo=Image(Point(200,100),"bitmap2.png")
    fundo.draw(win)
    entrada=Entry(Point(130,100),28)
    entrada.draw(win)
    entrada.setFill(color_rgb(255,255,255))
    text1=Text(Point(50,10),"")
    text1.draw(win)
    erro_esp=Image(Point(100,30),"bitmap8.png")
    text2=Text(Point(120,170),"")
    while key != "Escape":
        key=win.getKey()
        if key == "F1":
            ajuda()
        if key == "space":
            erro_esp.draw(win)
            text2.setText("Aperte 'CTRL' para continuar!")
            text2.draw(win)
            while key != "Control_L":
                key=win.getKey()
            text2.undraw()
            erro_esp.undraw()
            entrada.setText("")
        if key == "Return":
            texto2=(entrada.getText())+".egu"
            if " " in entrada.getText():
                causa="Não aceita arquivo com espaço!"
                exitcode=1
                erro(causa,exitcode)
            if len(entrada.getText()) == 0:
                causa="Não se aceita arquvio sem nome!"
                exitcode=1
                erro(causa,exitcode)
            entrada.undraw()
            alerta=Image(Point(200,100),"bitmap3.png")
            alerta.draw(win)
            text2=Text(Point(200,100),texto2)
            text2.draw(win)
            text2.setTextColor(color_rgb(255,255,255))
            text2.setSize(30)
            key=win.getKey()
            if key=="s":
                win.close()
                arquivo=open(file=texto2,mode="w",encoding="UTF=8")
                arquivo.write("---------------EGU--------------------\n")
                arquivo.close()
                win.close()
                return(texto2)
            else:
                alerta.undraw()
                entrada.draw(win)
                text2.undraw()
                entrada.setText("")
    win.close()
    arquivo=open(file="não_definido.egu",mode="w",encoding="UTF-8")
    arquivo.close()
    return("não_definido.egu")
#####################################################
def principal(nomearquivo):
    win=GraphWin(title="Simple Vote - Injetor",width=600,height=400)
    key=None
    fundo=Image(Point(300,200),"bitmap.png")
    fundo.draw(win)
    text1=Text(Point(50,10),"")
    text1.draw(win)
    count=0
    add_count=Text(Point(480,20),"Nenhum candidato adicionado!")
    add_count.draw(win)
    entrada1=Entry(Point(130,180),20)
    entrada1.setFill(color_rgb(255,255,255))
    entrada2=Entry(Point(370,180),20)
    entrada2.setFill(color_rgb(255,255,255))
    entrada3=Entry(Point(130,268),20)
    entrada3.setFill(color_rgb(255,255,255))
    entrada1.draw(win)
    entrada2.draw(win)
    entrada3.draw(win)
    erro3=Image(Point(200,50),"bitmap10.png")
    while key != "Escape":
        key=win.getKey()
        try:
            alert1.undraw()
        except:
            pass
        erro=0
        if key =="Return":
            candidato=entrada1.getText()
            numero=entrada2.getText()
            cargo=entrada3.getText()
            a=len(candidato)
            b=len(numero)
            c=len(cargo)
            if a <=2 or b !=4 or c<=0:
                erro=1
                entrada1.setText("")
                entrada2.setText("")
                entrada3.setText("")
                erro3.draw(win)
                win.getKey()
                erro3.undraw()
            if erro ==0:
             arquivo(nomearquivo,candidato,numero,cargo)
             print(nomearquivo,candidato,numero,cargo)
             count=count+1
             add_count.setText(str(count)+" Candidato(s) adicionado(s).")
             entrada1.setText("")
             entrada2.setText("")
             entrada3.setText("")
             alert1=Image(Point(200,35),"bitmap4.png")
             alert1.draw(win)
    win.close()
#####################################################
def arquivo(nomearquivo,candidato,numero,cargo):
    arquivo=open(file=nomearquivo,mode="a",encoding="UTF-8")
    arquivo.write(candidato+", "+numero+", "+cargo+"\n")
    arquivo.close()
####################################################
def cargo_conf(nomearquivo):
    win=GraphWin(title="Configurar Cargos",width=600,height=300)
    win.setBackground(color_rgb(199,0,36))
    intenal=Rectangle(Point(10,10),Point(590,290))
    intenal.setOutline(color_rgb(246,162,1))
    intenal.setFill(color_rgb(246,162,1))
    intenal.draw(win)
    text1=Text(Point(130,20),"")
    text1.draw(win)
    entrada=Entry(Point(300,150),25)
    entrada.draw(win)
    lista1=[]
    carg=1
    key=None
    Text3=Text(Point(300,130),"Inisira o nome do cargo e ele vai ser atribuido a um numero")
    Text3.draw(win)
    Text4=Text(Point(170,150),"")
    Text4.draw(win)
    entrada.setFill(color_rgb(255,255,255))
    texto5=Text(Point(190,230),"")
    texto6=Text(Point(260,270),"Enter => Para Salvar Cargos == Escape => Para Encerrar Adição ")
    texto6.draw(win)
    texto5.draw(win)
    while key!="Escape":
        Text4.setText(str(carg)+" =>")
        text1.setText("Definindo Cargo Nº "+str(carg))
        key=win.getKey()
        if key =="Return":
            gat=1
            if len(entrada.getText()) <=4:
                causa="Não se aceita arquvio sem nome ou nome invalido!"
                texto5.setText(causa+"\n Aperte qualquer tecla para descartar esse alerta!")
                texto5.setTextColor(color_rgb(255,0,0))
                win.getKey()
                texto5.setText("")
                entrada.setText("")
                gat=0
            if gat == 1:
             cargo=entrada.getText()
             cargo_n=carg
             cargo_n=str(cargo_n)
             tolist=cargo+", "+cargo_n
             lista1.append(tolist)
             entrada.setText("")
             carg=carg+1
    janela2=GraphWin(title="Checagem",width=600,height=700)
    fundo=Image(Point(300,350),"bitmap11.png")
    fundo.draw(janela2)
    texto7=Text(Point(300,350),"")
    texto7.draw(janela2)
    a=len(lista1)
    c=""
    for l in range (0,a):
        b=lista1[l]
        c=c+str(b)+"\n"
    texto7.setText(c)
    win.close()
    a=open(file=nomearquivo,mode="a",encoding="UTF-8")
    a.write(c+"---------------CFT--------------------\n")
    a.close()
    if len(lista1) >0:
     principal(nomearquivo)
    else:
        erro("Nenhum Cadidato Informado",1)
    janela2.close()
####################################################    
nomearquivo=arquivo_saida()
if nomearquivo == "não_definido.egu":
    sys.exit()
cargo_conf(nomearquivo)