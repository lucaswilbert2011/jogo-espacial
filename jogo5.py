#pgzero
import random

WIDTH = 600
HEIGHT = 300

player = Actor('hero', (400, 300), size=(70, 70))

star = Actor('star', size=(30, 30))
star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
enemies = []
for i in range (7):
    enemy = Actor('enemy', size=(30, 30))
    enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    enemy.speed_x = random.choice([2, -2])
    enemy.speed_y = random.choice([2, -2])
    enemies.append(enemy)


background = Actor('background')

score = 0
game_over = False 

def draw():
    screen.clear()
    background.draw()
    if not game_over:
        player.draw()
        star.draw()
        for enemy in enemies:
            enemy.draw()
        screen.draw.text(score, (10, 10), color='white')
    else:
        screen.draw.text('Você perdeu! Pressione R para reiniciar', center=(WIDTH // 2, HEIGHT // 2), fontsize=30, color='red')

def update(dt):
    global score, game_over, hero

    if game_over:
        if keyboard.R:
            restart_game()
        return

    if keyboard.left:
        if player.left > 0:
            player.x -= 10
    if keyboard.right:
        if player.right < WIDTH:
            player.x += 10
    if keyboard.up:
        if player.top > 0:
            player.y -= 10
    if keyboard.down:
        if player.bottom < HEIGHT:
            player.y += 10

    if player.colliderect(star):
        game_over = True
        

    for enemy in enemies:
        enemy.x += enemy.speed_x
        enemy.y += enemy.speed_y

        if enemy.left < 0:
            enemy.speed_x = -enemy.speed_x
        if enemy.right > WIDTH:
            enemy.speed_x = -enemy.speed_x
        if enemy.top < 0:
            enemy.speed_y = -enemy.speed_y
        if enemy.bottom > HEIGHT:
            enemy.speed_y = -enemy.speed_y

        if player.colliderect(enemy):
            score += 1
            star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)

def restart_game():
    global score, game_over
    player.pos = 400, 300
    star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    for enemy in enemies:
        enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
        enemy.speed_x = random.choice([2, -2])
        enemy.speed_y = random.choice([2, -2])
    score = 0
    game_over = False