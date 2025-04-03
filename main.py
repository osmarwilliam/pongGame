from PPlay.window import *
from PPlay.sprite import *

janela = Window(1240, 600)
janela.set_title("OsmarWilliam")
bolinha = Sprite("bola.png", 1)

while(True):
    janela.set_background_color((0,0,255))
    bolinha.set_position(1240/2, 600/2)
    bolinha.draw()
    janela.update()
