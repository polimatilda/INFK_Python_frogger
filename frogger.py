# hasznaljuk a pygame libraryt
import pygame
# hasznaljuk az osszes erteket a locals filebol pl.: gombok kezelese
from pygame.locals import *

# Kotelezo lepes a pygame lib hasznalatanal ez allitja ossze az alapokat
pygame.init()

# Beallitjuk az abalak mereteit es feliratait
WIDTH, HEIGHT = 550, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Frogger_PM')

# Kepek importalasa

hatter = pygame.image.load('hatter.jpg')
hatter_h = 650
hatter_w = 550
hatter = pygame.transform.scale(hatter, (hatter_w, hatter_h))

beka = pygame.image.load('beka.png')
beka_h = 75
beka_w = 75
beka = pygame.transform.scale(beka, (beka_w, beka_h))

level = pygame.image.load('level.png')
level_h = 115
level_w = 115
level = pygame.transform.scale(level, (level_w, level_h))


# Itt definialjuk a konstansokat
WHITE = (255, 255, 255)
GREEN = ('#8edc83')
VEL = 1
FPS = 60

# Segitseg az iranyitashoz 
pygame.key.set_repeat(1)

def main():
    # Beallitjuk a kepkocka sebesseget, mert kulonbozo CPU-kon kolonbozo 
    # sebesseggel futhat a jatek
    clock = pygame.time.Clock()
    
    # Kepek befoglalo negszogenek beallitasa
    hatter_rect = pygame.Rect(0, 0, hatter_w, hatter_h)
    beka_rect = pygame.Rect(225, 575, beka_w, beka_h)
    level_rect = pygame.Rect(225, 0, level_w, level_h)
    
    # bejutott bekak szamlalojanak beallitasa - alapertekek
    beka_szam = 0
    is_connected = False

    # Vegtelen ciklus, ami eletben tarja az ablakot, egyebkent rogton bezarodna 
    # az ablaak, amit fent letrehoztunk, mert veget erna a program
    run = True
    while run:
        # Itt tartjuk kordaban az FPS-t
        clock.tick()
        # Itt ellenorizzuk hogy tortent-e valamilyen esemeny ez az esemeny lehet 
        # gombnyomas, eger mozgatas, kattintas, ablak mozgatas
        for event in pygame.event.get():
            # Ez az if ellenorzi, h rakattintottunk-e az x gombra az ablakon
            if event.type == pygame.QUIT:
                # Ha rakattintunk az x-re, akkor vege a vegtelen ciklusnak
                run = False
             
            # Beka mozgasanak beallitasa             
            if event.type == KEYDOWN:
                if event.key ==K_d:
                    beka_rect.x += VEL
                if event.key ==K_a:
                    beka_rect.x -= VEL
                if event.key ==K_w:
                    beka_rect.y -= VEL
                if event.key ==K_s:
                    beka_rect.y += VEL
         
        # bejutott bekak szamlalojanak elkeszitese         
        if level_rect.colliderect(beka_rect) and (is_connected == False):
            beka_szam += 1
            is_connected = True
            
        if not level_rect.colliderect(beka_rect):
            is_connected = False
            
        # szoveg definialasa, bejuttatott bekak szama
        font = pygame.font.Font('freesansbold.ttf', 14)
        beka_szamlalo = font.render(f'Átjuttatott békák száma: {beka_szam}', True, GREEN)
        beka_szamlalo_rect = beka_szamlalo.get_rect()
        beka_szamlalo_rect.x = 10
        beka_szamlalo_rect.y = 20

        # Beallitjuk a hatterer szinet
        WIN.fill(WHITE)
              
        # Kepek megjelenitese
        WIN.blit(hatter, (hatter_rect.x, hatter_rect.y))
        WIN.blit(level, (level_rect.x, level_rect.y))
        WIN.blit(beka, (beka_rect.x, beka_rect.y))
        
        #szoveg kiirasa
        WIN.blit(beka_szamlalo, (beka_szamlalo_rect.x, beka_szamlalo_rect.y))

        # Frissitjuk a teljes kepernyot, hogy ha valtozna valami akkor az megjelenjen
        pygame.display.update()

    # Lezarjuk az inicializalt funkciokat ,amit a pygame.init() letrehozott
    pygame.quit()

# Futtatjuk a fenti main fugvenyt, ha ezt a fajlt futtatjuk
if __name__ == '__main__':
    main()

