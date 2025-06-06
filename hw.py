import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('My first game screen')
screen.fill((0, 0, 0))

font = pygame.font.SysFont('Arial', 40, bold=True)
text = font.render('I am displaying text with help of pygame', True, (200, 243, 243))
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    pygame.draw.rect(screen, (255, 153, 102), pygame.Rect(200, 150, 100, 60))
    txt_rect = text.get_rect(center=(320, 240))
    screen.blit(text, txt_rect)

    pygame.display.update()

pygame.quit()

    
            
