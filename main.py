from PPlay.window import *
import random
import time

janela = Window(1240, 600)
janela.set_title("OsmarWilliam")

while(True):
    janela.set_background_color((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
    janela.update()
    time.sleep(1)