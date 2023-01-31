import pygame
pygame.init()

screen = pygame.display.set_mode((750, 500))
pygame.display.set_caption('Ping Pong')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255,0,0)
blue = (0,0,255)


class paletka1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 120])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.points = 0

class paletka2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 120])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.points = 0

class Piłka(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.speed = 20
        self.dx = 1
        self.dy = 1


#rozmiary paletek

paletka1 = paletka1()
paletka1.rect.x = 25
paletka1.rect.y = 225

paletka2 = paletka2()
paletka2.rect.x = 715
paletka2.rect.y = 225

paletka_speed = 15

piłka = Piłka()
piłka.rect.x = 375
piłka.rect.y = 250


all_sprites = pygame.sprite.Group()
all_sprites.add(paletka1, paletka2, piłka)



def redraw():
    screen.fill(black)

    font = pygame.font.SysFont('fantasy', 40)
    text = font.render('PING PONG ', False, white)
    textRect = text.get_rect()
    textRect.center = (750 // 2, 25)
    screen.blit(text, textRect)

    #GRACZ 1
    p1_score = font.render(str(paletka1.points), False, white)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (50, 50)
    screen.blit(p1_score, p1Rect)

    #GRACZ 2
    p2_score = font.render(str(paletka2.points), False, white)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (700, 50)
    screen.blit(p2_score, p2Rect)

    all_sprites.draw(screen)

    pygame.display.update()

run = True

while run:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paletka1.rect.y += -paletka_speed
    if key[pygame.K_s]:
        paletka1.rect.y += paletka_speed
    if key[pygame.K_UP]:
        paletka2.rect.y += -paletka_speed
    if key[pygame.K_DOWN]:
        paletka2.rect.y += paletka_speed

    piłka.rect.x += piłka.speed * piłka.dx
    piłka.rect.y += piłka.speed * piłka.dy

#odbijanie

    if piłka.rect.y > 490:
        piłka.dy = -1

    if piłka.rect.y < 1:
        piłka.dy = 1

    if piłka.rect.x > 740:
        piłka.rect.x, piłka.rect.y = 375, 250
        piłka.dx = -1
        paletka1.points += 1

    if piłka.rect.x < 1:
        piłka.rect.x, piłka.rect.y = 375, 250
        piłka.dx = 1
        paletka2.points += 1

    if paletka1.rect.colliderect(piłka.rect):
        piłka.dx = 1

    if paletka2.rect.colliderect(piłka.rect):
        piłka.dx = -1

    redraw()

pygame.quit()

