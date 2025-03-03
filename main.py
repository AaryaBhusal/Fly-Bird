#Import all the necessary modules
from pygame import *
from random import randint

#Create some Constants
GAME_HEIGHT = 600
GAME_WIDTH = 700
GRAVITY = 3
SPEED = 3
PIPE_GAP = 300
JUMP = 80

init()
clock = time.Clock()
display.set_caption("Fly Bird")
screen = display.set_mode((GAME_WIDTH, GAME_HEIGHT))
logo = image.load("bird.png").convert_alpha()
bird = transform.scale(logo, (50, 50))
display.set_icon(logo)
background = image.load("background.jpg")
background = transform.scale(background, (GAME_WIDTH, GAME_HEIGHT))
bird_x, bird_y = 50, 100
pipe_height, pipe_up_height  = randint(60, 230), randint(60, 230)
pipe2_height, pipe2_up_height = randint(60, 100), randint(300, 370)
pipe3_height, pipe3_up_height = randint(300, 370), randint(60, 100)
pipe_x = 600
pipe2_x = pipe_x + PIPE_GAP
pipe3_x = pipe2_x + PIPE_GAP
pipe1_color = (randint(0, 255), randint(0, 255), randint(0, 255))
pipe2_color = (randint(0, 255), randint(0, 255), randint(0, 255))
pipe3_color = (randint(0, 255), randint(0, 255), randint(0, 255))
defultfont = font.Font(None, 25)
game_over_text = defultfont.render("Game Over! Press R to Restart.", True, (0,0,0))
score = 0
running = True
game_over = False
game_over_music = False
game_start = True


while running:
    if game_start:
        mixer.init()
        mixer.music.load("start.mp3")
        mixer.music.set_volume(1)
        mixer.music.play()
        game_start = False

    for events in event.get():
        if events.type == QUIT:
            running = False
        elif events.type == KEYDOWN:
            if events.key == K_SPACE and not game_over:
                bird_y-=JUMP
    screen.blit(background, (0,0))
    screen.blit(bird, (bird_x, bird_y)) 

    pipe = draw.rect(screen, pipe1_color, (pipe_x, GAME_HEIGHT-pipe_height, 50, pipe_height))
    pipe2 = draw.rect(screen, pipe2_color, (pipe2_x, GAME_HEIGHT-pipe2_height, 50, pipe2_height))
    pipe3 = draw.rect(screen, pipe3_color, (pipe3_x, GAME_HEIGHT-pipe3_height, 50, pipe3_height))

    pipe_up = draw.rect(screen, pipe1_color, (pipe_x, 0, 50, pipe_up_height))
    pipe2_up = draw.rect(screen, pipe2_color, (pipe2_x,0, 50, pipe2_up_height))
    pipe3_up = draw.rect(screen, pipe3_color, (pipe3_x, 0, 50, pipe3_up_height))

    if game_over:
        if game_over_music:
            mixer.init()
            mixer.music.load("game_over.mp3")
            mixer.music.set_volume(1)
            mixer.music.play()
            game_over_music = False
        screen.blit(game_over_text, ((GAME_WIDTH//2)-120, GAME_HEIGHT//2))
        keys = key.get_pressed()
        if keys[K_r]:
            score = 0
            bird_x, bird_y = 50, 100
            pipe_height, pipe_up_height  = randint(60, 230), randint(60, 230)
            pipe2_height, pipe2_up_height = randint(60, 100), randint(300, 370)
            pipe3_height, pipe3_up_height = randint(300, 370), randint(60, 100)
            pipe_x = 600
            pipe2_x = pipe_x + PIPE_GAP
            pipe3_x = pipe2_x + PIPE_GAP
            pipe1_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            pipe2_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            pipe3_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            game_start = True
            game_over = False
    if not game_over: 
        bird_y+= GRAVITY
        pipe_x-=SPEED
        pipe2_x-=SPEED
        pipe3_x-=SPEED

        if pipe_x<= -50:
            pipe1_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            score+=1
            pipe_x=GAME_WIDTH+100
            pipe_height = randint(60, 230)
            pipe_up_height = randint(60, 230)
        if pipe2_x <= -50:
            pipe2_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            score+=1
            pipe2_x=GAME_WIDTH
            pipe2_height = randint(60, 100)
            pipe2_up_height = randint(300, 370)
        if pipe3_x <= -50:
            pipe3_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            score+=1
            pipe3_x=GAME_WIDTH
            pipe3_height = randint(300, 370)
            pipe3_up_height = randint(60, 100)
        
        bird_rectangle = Rect(bird_x, bird_y, 50, 50)
        if(bird_rectangle.colliderect(pipe) or bird_rectangle.colliderect(pipe2) or bird_rectangle.colliderect(pipe3) or bird_rectangle.colliderect(pipe_up) or bird_rectangle.colliderect(pipe2_up) or bird_rectangle.colliderect(pipe3_up)) or (bird_y>= GAME_HEIGHT or bird_y<=-40):
            game_over = True
            game_over_music = True
    score_text = defultfont.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (0,0)) 

    clock.tick(70)
    display.flip()

quit()