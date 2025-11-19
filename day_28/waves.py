import pygame
import math
pygame.init()
s = pygame.display.set_mode((600, 400))
c = pygame.time.Clock()
run = True
t = 0

while run:
    s.fill((0, 0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    for x in range(0, 600, 5):
        y = 200+50*math.sin(0.05*x+t)
        pygame.draw.circle(s, (0, 255, 255), (x, int(y)), 3)
    t += 0.2
    pygame.display.flip()
    c.tick(60)
pygame.quit()
