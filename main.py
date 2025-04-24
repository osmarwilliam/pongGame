from PPlay.window import *
from PPlay.sprite import *
import random

# gerando janela do jogo
janela = Window(1240, 650)
janela.set_title("OsmarWilliam")

# criando elementos da interface
bolinha = Sprite("ball.png", 1)
bar1 = Sprite("bar.png", 1)
bar2 = Sprite("bar.png", 1)
bar_vertical = Sprite("bar.png", 1)


# posicionando os elementos na tela
bolinha.set_position(janela.width/2 - bolinha.width/2, janela.height/2- bolinha.height/2)
bar1.set_position(bar1.width, janela.height/2 - bar1.height /2)
bar2.set_position(janela.width - 2*bar2.width, janela.height/ 2 - bar2.height/2)
bar_vertical.set_position(janela.width, janela.height)

ponto_jogador = 0
ponto_ia = 0

velx = 0
vely = 0
barra_ia_vel = 0
keyboard = janela.get_keyboard()
tempo = 0
count = 0
cronometro = 0

while(True):
    # quando SPACE for pressionado o jogo irá começar
    if (keyboard.key_pressed("SPACE")):
        velx = -400
        vely = -400
        # caso queira deixar aumentar a dificuldade basta mudar a velocidade da ia
        barra_ia_vel = random.randint(330,350) 
        count = 0
        tempo = 0

    # pressione ESC para fechar o jogo
    if keyboard.key_pressed("ESC"):
        break

    # movendo a barra com as teclas UP e DOWN
    if keyboard.key_pressed("UP") and bar1.y > 0:
        bar1.y -= 400 * janela.delta_time()
    if keyboard.key_pressed("DOWN") and bar1.y < janela.height - bar1.height:
        bar1.y += 400 * janela.delta_time()

    # controla a colisão da bolinha com as barras
    if bar1.collided(bolinha):
        count += 1
        if velx <= 1000 and velx >= -1000:
            velx *= -1.08
            bolinha.x = bar1.x + bar1.width
        else:
            velx *= -1
            bolinha.x = bar1.x + bar1.width

    if bar2.collided(bolinha):
        count += 1
        if velx <= 1000 and velx >= -1000: 
            velx *= -1.08
            bolinha.x = janela.width - 2*bar2.width - bolinha.width
        else:
            velx *= -1
            bolinha.x = janela.width - 2*bar2.width - bolinha.width
        
    tempo += janela.delta_time()

    if (count == 3):
        bar_vertical.set_position(janela.width/2 - bar_vertical.width/2, random.randint(0, 650 - 100))
        count += 1
        cronometro = (random.randint(3,5)) 
        tempo = 0
    
    if (count >= 3):
        if bar_vertical.collided(bolinha):
            if velx <= 1200 and velx >= -1200:
                velx *= -1.08
            else:
                velx *= -1
        if (tempo > cronometro):
            bar_vertical.set_position(janela.width, janela.height)
            count = 0

    # movimenta a bolinha pelo eixo x e y    
    bolinha.x += velx * janela.delta_time()
    bolinha.y += vely * janela.delta_time()

    # controle da colisao da bolinha com o limite superior ou lateral    
    if bolinha.y <= 0:
        vely *= -1
        bolinha.y = 1 # impede o deslizamento
    if bolinha.y >= janela.height - bolinha.height:
        vely *= -1
        bolinha.y = janela.height - bolinha.height - 1 # impede o deslizamento

    # controle da bolinha caso ela ultrapasse os limites laterais, somando o placar e retornando ela ao centro
    if bolinha.x >= janela.width - bolinha.width:
        velx = 0
        bolinha.set_position(janela.width/2 - bolinha.width/2, janela.height/2- bolinha.height/2)
        bar2_vel = 0 
        vely = 0
        bar2.set_position(janela.width - 2*bar2.width, janela.height/ 2 - bar2.height/2)
        ponto_jogador += 1
    if bolinha.x <= 0:
        velx = 0
        vely = 0
        bolinha.set_position(janela.width/2 - bolinha.width/2, janela.height/2- bolinha.height/2)
        bar2_vel = 0
        ponto_ia += 1
        bar2.set_position(janela.width - 2*bar2.width, janela.height/ 2 - bar2.height/2)

    
    # para centralizar no meio da barra a colisão
    barra_central = bar2.y + bar2.height / 2

    if bolinha.y < barra_central - 10:
        bar2.y -= barra_ia_vel * janela.delta_time()
    if bolinha.y > barra_central + 10:
        bar2.y += barra_ia_vel * janela.delta_time()
    # controla a barra da ia para não ultrapassar os limites
    if bar2.y < 0:
        bar2.y = 0    
    if bar2.y > janela.height - bar2.height:
        bar2.y = janela.height - bar2.height

    # Atualiza o cenário
    janela.set_background_color((0,0,255))
    bar1.draw()
    bar2.draw()
    bolinha.draw()
    bar_vertical.draw()

    # exibe o placar na tela
    janela.draw_text(str(ponto_jogador), (janela.width/4), (janela.height/5),size=70, color=(255,0,0), font_name= "ponto_jogador", bold=False, italic=False)
    janela.draw_text(str(ponto_ia), 2* (janela.width/3), (janela.height/5),size=70, color=(255,0,0), font_name= "p", bold=False, italic=False)
    
    janela.update()