import pygame
from core.game import GameInstance
    
if __name__ == '__main__':
    # pygame init 
    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((
        width,
        height
    ), pygame.DOUBLEBUF)
    mask = pygame.surface.Surface((
        width,
        height
    ), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SRCALPHA, 32)
    # mask.fill((0, 0, 0))
    
    game_instance = GameInstance(width, height)
    
    running = True
    clock = pygame.time.Clock()
    dt = 0

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False 
                 
        mask.fill((0, 0, 0))
        
        for index, value in enumerate(game_instance.render()):
            (start, end), color = value
            pygame.draw.line(mask, color, [index, start], [index, end], 1)
        
        pygame.draw.circle(mask, (255, 255, 255), [width / 2, height / 2], 3)
    
        screen.blit(mask,(0, 0))
        
        clock.tick(60)
        # dt = clock.get_rawtime() / 1000
        dt = clock.get_time() / 1000
        fps = clock.get_fps()
        # print(dt)
        move_speed = dt * 2
        rotate_speed = dt * 3
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            game_instance.move(move_speed)
        if keys[pygame.K_DOWN]:
            game_instance.move(move_speed, forward=False)
        if keys[pygame.K_LEFT]:
            game_instance.rotate(rotate_speed, clockwise=False)
        if keys[pygame.K_RIGHT]:
            game_instance.rotate(rotate_speed)
        
        pygame.display.flip()

    pygame.quit()