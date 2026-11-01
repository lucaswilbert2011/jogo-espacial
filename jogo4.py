#pgzero
import random
WIDTH = 600 #largura da janela
HEIGHT = 300 #Altura da janela
TITLE = "Titulo do Jogo"
FPS = 30 # Frames por segundos
# objetos - primeiro vem o nome da imagem, segundo a posição e terceiro se for o caso use o size = (x,y) para determinar o tamanho da imagem
background = Actor("background", size = (600,300))
player = Actor("player", (300,150), size = (50,50)) 

enemies = []

for i in range(3):
    x = random.randint(0, 600)
    y = random.randint(0, 300)
    enemy = Actor("enemy", (x,y), size = (50,50))
    enemy.speed = 1
    enemies.append(enemy)

go = Actor("game_over", size = (600,300))
mode = "game"
count = 0
def draw(): # desenhando elementos na tela
    if mode == "game":# modo game
        background.draw()#sempre o background primeiro
        for enemy in enemies:
            enemy.draw()
        screen.draw.text("Fuja!", center = (300,20), color = "white", fontsize = 16) # desenhando texto na tela (nesse exemplo pontuação)
        player.draw()    
    elif mode == "game_over":# modo game over
        go.draw()
def update(dt):
    global mode, count
    # controles teclado(se for o caso)
    if keyboard.left: # vai se movimentar pela seta do teclado(esse é para esquerda)
        player.x -= 5
        player.image = "astr.left"
    elif keyboard.right:# vai se movimentar pela seta do teclado(esse é para direita)
        player.x += 5
        player.image = "astr_right"
    elif keyboard.up:
        player.y -= 5
        player.image = "player"
    elif keyboard.down:
        player.y += 5
        player.image ="player"
    # movimentação do inimigo (OBS: Se for um jogo tipo nave, você pode mudar o eixo de X para Y a movimentação)

    for i in range(len(enemies)):
         if enemies[i].x > -20:
             enemies[i].x = enemies[i].x - 5 # aqui basicamente, o inimigo se move para esquerda a cada atualização de frame
         else:
             enemies[i].x = WIDTH + 20 # aqui faz com que o inimigo volte para uma posição fora da tela para recomeçar
             count += 1
    # colisão
    enemy_indice = player.collidelist(enemies)
    if enemy_indice > 0:
   
        # Logica de game_over ou dano ao personagem(pode alterar também a imagem do player para ficar mais legal)
        mode = "game_over" 
    # reinicio do jogo
    if mode == "game_over" and keyboard.R:
        mode = "game"

        