from graphics import *


def creditos():
    janela = GraphWin(title="Creditos", width=(500), height=(500))
    fundo = Image(Point(250, 250), "bitmap19.png")
    fundo.draw(janela)
    janela.getKey()
    janela.close()
