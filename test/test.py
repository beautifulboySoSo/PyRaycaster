# a = {
#     'name': 'lee',
#     'age': 10,
# }
# b = {
#     **a,  
#     'name': 'lee2'
# }
# b = {
#     i: a.get(i) for i in a.keys() - {'name'}
# }
# # b = {1, 2, 3}
# print(b.keys())

# render_buffer = [[
#     # (draw_start, draw_end)
#     (0, 0),
#     # rgba
#     (0, 0, 0, 255)
# ] for _ in range(3)]

# print(render_buffer)

import pygame

if __name__ == '__main__':
    # pygame init 
    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((
        width,
        height
    ))
    mask = pygame.surface.Surface((
        width,
        height
    ), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SRCALPHA)
    # mask.fill((0, 0, 0))
    # mask.set_alpha(150)
    
    pygame.draw.circle(mask, (0, 255, 0, 5), [width / 2, height / 2], 200)
    # print(mask.get_alpha())
    
    running = True


    while running:

        screen.blit(mask, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False  
                
        # screen.fill((0, 0, 0))
        
        
        pygame.display.flip()

    pygame.quit()
