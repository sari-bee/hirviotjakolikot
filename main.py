class Robotti:
    def __init__(self):
        self.robotti = pygame.image.load("robo.png")
        self.y = 400 - self.robotti.get_height()
        self.x = 300

    def robotti(self):
        return self.robotti
    
    def liiku_oikealle(self):
        if self.x + self.robotti.get_width() >= 600:
            pass
        else:
            self.x+=4
    def liiku_vasemmalle(self):
        if self.x <= 0:
            pass
        else:
            self.x-=4

    def x(self):
        return self.x

    def y(self):
        return self.y

class Kolikko:
    def __init__(self, nopeus: int):
        self.kolikko = pygame.image.load("kolikko.png")
        self.y = 0
        self.x = random.randint(0, 600 - self.kolikko.get_width())
        self.nopeus1 = nopeus
        self.nopeus2 = nopeus

    def kolikko(self):
        return self.robotti

    def x(self):
        return self.x

    def y(self):
        return self.y

class Hirvio:
    def __init__(self, nopeus: int):
        self.hirvio = pygame.image.load("hirvio.png")
        self.y = 0
        self.x = random.randint(0, 600 - self.hirvio.get_width())
        self.nopeus1 = nopeus
        self.nopeus2 = nopeus

    def hirvio(self):
        return self.hirvio

    def x(self):
        return self.x

    def y(self):
        return self.y

import pygame
import random
pygame.init()
naytto = pygame.display.set_mode((600, 400))
font = pygame.font.SysFont("Courier", 18)
pygame.display.set_caption("Älä hukkaa kolikkoa! Varo hirviötä! Robotti liikkuu nuolinäppäimillä.")
robotti = Robotti()
kolikko = Kolikko(2)
hirvio = Hirvio(2)

kello = pygame.time.Clock()

oikealle = False
vasemmalle = False

osumat = 0

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False

    if oikealle:
        robotti.liiku_oikealle()
    if vasemmalle:
        robotti.liiku_vasemmalle()

    naytto.fill((0, 0, 50))
    naytto.blit(robotti.robotti, (robotti.x, robotti.y))
    naytto.blit(kolikko.kolikko, (kolikko.x, kolikko.y))
    naytto.blit(hirvio.hirvio, (hirvio.x, hirvio.y))
    pygame.display.flip()

    kolikko.y += kolikko.nopeus1
    kolikko.x += kolikko.nopeus2
    hirvio.y += hirvio.nopeus1
    hirvio.x -= hirvio.nopeus2

    if kolikko.y+kolikko.kolikko.get_height() >= 400 or (hirvio.y+hirvio.hirvio.get_height() >= robotti.y and hirvio.x >= robotti.x and hirvio.x <= robotti.x+robotti.robotti.get_width()):
        hirvio.nopeus1 = 0
        hirvio.nopeus2 = 0
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False
        if kolikko.y+kolikko.kolikko.get_height() < 400:
            kolikko.nopeus1 = 0
            kolikko.nopeus2 = 0
        fontti = pygame.font.SysFont("Courier", 36)
        teksti = fontti.render("GAME OVER", True, (255, 255, 255))
        naytto.blit(teksti, (185, 125))
        teksti2 = font.render("pisteet " + str(osumat), True, (255, 255, 255))
        naytto.blit(teksti2, (230, 200))
        pygame.display.flip()
    if kolikko.x+kolikko.kolikko.get_width() >= 600 or kolikko.x <= 0:
        kolikko.nopeus2 = -kolikko.nopeus2
    if kolikko.y <= 0:
        kolikko.nopeus1 = -kolikko.nopeus1
    if kolikko.y+kolikko.kolikko.get_height() == robotti.y and kolikko.x >= robotti.x-25 and kolikko.x <= robotti.x+robotti.robotti.get_width():
        kolikko.nopeus1 = -kolikko.nopeus1
        osumat +=1

    if hirvio.x+hirvio.hirvio.get_width() >= 600 or hirvio.x <= 0:
        hirvio.nopeus2 = -hirvio.nopeus2
    if hirvio.y+hirvio.hirvio.get_height() >= 400 or hirvio.y <= 0:
        hirvio.nopeus1 = -hirvio.nopeus1

    kello.tick(60)