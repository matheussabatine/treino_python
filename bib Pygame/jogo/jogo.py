import pygame

#setup

pygame.init()
screen= pygame.display.set_mode((1280, 720))
clock= pygame.time.Clock()
running= True
#delta time
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    #eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("purple")

    #render
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt


    pygame.display.flip()

    #limita FPS a 60
    clock.tick(60)
     # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
pygame.quit()
