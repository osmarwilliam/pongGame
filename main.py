from PPlay.window import *
from PPlay.sprite import *

janela = Window(1240, 600)
janela.set_title("OsmarWilliam")
bolinha = Sprite("ball.png", 1)

bolinha.set_position(janela.width/2 - bolinha.width/2, janela.height/2- bolinha.height/2)

velx = 2
vely = 2

keyboard = janela.get_keyboard()

comecar = False

while(True):

    if (keyboard.key_pressed("SPACE")):
        comecar = True

    if(comecar):
        if keyboard.key_pressed("ESC"):
            break

        bolinha.x += velx
        bolinha.y += vely 

        if bolinha.x >= janela.width - bolinha.width:
            if velx <= 5 and velx >= -5: 
                velx *= -1.1
            else:
                velx *= -1

        if bolinha.x <= 0:
            if velx <= 5 and velx >= -5:
                velx *= -1.1
            else:
                velx *= -1

        if bolinha.y <= 0:
            vely *= -1
        if bolinha.y >= janela.height - bolinha.height:
            vely *= -1

    janela.set_background_color((0,0,255))
    bolinha.draw()
    janela.update()