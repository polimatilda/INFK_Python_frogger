# hasznaljuk a pygame libraryt
import pygame
# hasznaljuk az osszes erteket a locals filebol pl.: gombok kezelese
from pygame.locals import *

# randint method random moduljanak importalasa
from random import randint

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
beka_h = 58
beka_w = 75
beka = pygame.transform.scale(beka, (beka_w, beka_h))

level = pygame.image.load('level.png')
level_h = 105
level_w = 115
level = pygame.transform.scale(level, (level_w, level_h))

auto1 = pygame.image.load('auto.png')
auto1_h = 75
auto1_w = 108
auto1 = pygame.transform.scale(auto1, (auto1_w, auto1_h))

auto2 = pygame.image.load('auto2.png')
auto2_h = 75
auto2_w = 108
auto2 = pygame.transform.scale(auto2, (auto2_w, auto2_h))

auto3 = pygame.image.load('auto.png')
auto3_h = 75
auto3_w = 108
auto3 = pygame.transform.scale(auto3, (auto3_w, auto3_h))

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
    
    # idohoz alapertekek beallitasa
    masodperc_szam = 0
    kattanas_szamlalo = 0
    
    # Kepek befoglalo negszogenek beallitasa
    hatter_rect = pygame.Rect(0, 0, hatter_w, hatter_h)
    beka_rect = pygame.Rect(240, 590, beka_w, beka_h)
    level_rect = pygame.Rect(225, 0, level_w, level_h)
    auto1_rect = pygame.Rect(500, 470, auto1_w, auto1_h)
    auto2_rect = pygame.Rect(-50, 300, auto2_w, auto2_h)
    auto3_rect = pygame.Rect(500, 130, auto3_w, auto3_h)
    
    # autok mozgasahoz szukseges default beallitasok
    direction_1 = -1
    direction_2 = 1
    direction_3 = -1
    speed_x_1 = 1
    speed_x_2 = 2
    speed_x_3 = 3
    
    # bejutott bekak szamlalojanak beallitasa - alapertekek
    beka_szam = 0
    eletek = 3
    is_connected = False

    # Vegtelen ciklus, ami eletben tarja az ablakot, egyebkent rogton bezarodna 
    # az ablaak, amit fent letrehoztunk, mert veget erna a program
    run = True
    
    while run:
    
        # Itt tartjuk kordaban az FPS-t
        clock.tick(60)
        
        # jatekido szamlalasa
        kattanas_szamlalo += 1
        if kattanas_szamlalo == 60:
            masodperc_szam += 1
            kattanas_szamlalo = 0
        
        font = pygame.font.Font('freesansbold.ttf', 14)
        ido_szoveg = font.render(str(masodperc_szam), True, WHITE)
        ido_rect = ido_szoveg.get_rect()
        ido_rect.x = 500
        ido_rect.y = 620
        
        # elso auto mozgasa
        if auto1_rect.right <= -50 or auto1_rect.left >= 600:
            direction_1 *= -1
            speed_x_1 = randint(1, 3) * direction_1
            
        if speed_x_1 == 0:
            speed_x_1 = randint(1, 3) * direction_1 
        
        if auto1_rect.right == 550:
            auto1_rect.right <= 0
            
        if auto1_rect.right == 0:
            auto1_rect = pygame.Rect(500, 470, auto1_w, auto1_h)

        auto1_rect.right += speed_x_1 * direction_1
        pygame.draw.rect(WIN, (0,   255,   0), auto1_rect)
        
        # masodik auto mozgasa
        #if auto2_rect.left <= 0 or auto2_rect.right >= 550:
        #   direction_2 *= 1
        #   speed_x_2 = randint(1, 3) * direction_2
            
        if speed_x_2 == 0:
            speed_x_2 = randint(1, 3) * direction_2
        
        if auto2_rect.left == 550:
            auto2_rect.left <= 0
            
        if auto2_rect.left == 550:
            auto2_rect = pygame.Rect(-50, 300, auto2_w, auto2_h)
           
        auto2_rect.left += speed_x_2 * direction_2
        pygame.draw.rect(WIN, (0,   255,   0), auto2_rect)
        
        # harmadik auto mozgasa
        #if auto3_rect.right <= -30 or auto3_rect.left >= 600:
         #   direction_3 *= -1
          #  speed_x_3 = randint(1, 3) * direction_3
            
        if speed_x_3 == 0:
            speed_x_3 = randint(1, 3) * direction_3  
        
        if auto3_rect.right == 550:
            auto3_rect.right <= 0
            
        if auto3_rect.right == -10:
            auto3_rect = pygame.Rect(500, 130, auto3_w, auto3_h)
           
        auto3_rect.right += speed_x_3 * direction_3
        pygame.draw.rect(WIN, (0,   255,   0), auto3_rect)

        # Itt ellenorizzuk hogy tortent-e valamilyen esemeny ez az esemeny lehet 
        # gombnyomas, eger mozgatas, kattintas, ablak mozgatas
        for event in pygame.event.get():
            # kilepes az x-re kattintva
            if (event.type == pygame.QUIT or
            # kilepes ESC billenytuvel
            (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                run = False
             
            # Beka mozgasanak beallitasa AWSD            
            if event.type == KEYDOWN:
                if event.key ==K_d:
                    beka_rect.x += VEL
                if event.key ==K_a:
                    beka_rect.x -= VEL
                if event.key ==K_w:
                    beka_rect.y -= VEL
                if event.key ==K_s:
                    beka_rect.y += VEL
                    
            # beka mozgatasa nyilakkal
            if event.type == KEYDOWN:
                if event.key ==K_RIGHT:
                    beka_rect.x += VEL
                if event.key ==K_LEFT:
                    beka_rect.x -= VEL
                if event.key ==K_UP:
                    beka_rect.y -= VEL
                if event.key ==K_DOWN:
                    beka_rect.y += VEL
                         
        # bejutott bekak szamlalojanak elkeszitese         
        if level_rect.colliderect(beka_rect) and (is_connected == False):
            beka_szam += 1
            is_connected = True
            #pygame.time.wait(1000)
            beka_rect = pygame.Rect(240, 590, beka_w, beka_h)
            
        if not level_rect.colliderect(beka_rect):
            is_connected = False
            
        # utkozes autokkal, eletvesztes
        if auto1_rect.colliderect(beka_rect):
            #pygame.time.wait(1000)
            eletek -= 1
            beka_rect = pygame.Rect(240, 590, beka_w, beka_h)
                        
        if auto2_rect.colliderect(beka_rect):
            #pygame.time.wait(1000)
            eletek -= 1
            beka_rect = pygame.Rect(240, 590, beka_w, beka_h)
                        
        if auto3_rect.colliderect(beka_rect):
            #pygame.time.wait(1000)
            eletek -= 1
            beka_rect = pygame.Rect(240, 590, beka_w, beka_h)
                               
        # szoveg definialasa, bejuttatott bekak szama
        font = pygame.font.Font('freesansbold.ttf', 14)
        beka_szamlalo = font.render(f'Átjuttatott békák száma: {beka_szam}', True, GREEN)
        beka_szamlalo_rect = beka_szamlalo.get_rect()
        beka_szamlalo_rect.x = 10
        beka_szamlalo_rect.y = 20
        
        # harom beka bejutasakor gyozelem, a jatek ujrakezdodik
        if beka_szam == 3:
            #pygame.time.wait(1000)
            return main()
        
        # elet szamlalo
        font = pygame.font.Font('freesansbold.ttf', 14)
        elet_szamlalo = font.render(f'Életek: {eletek}', True, GREEN)
        elet_szamlalo_rect = elet_szamlalo.get_rect()
        elet_szamlalo_rect.x = 10
        elet_szamlalo_rect.y = 40
        
        # ha haromszor eluti a bekat egy auto, a jatek ujraindul
        if eletek == 0:
            #pygame.time.wait(1000)
            return main()
                
        # Beallitjuk a hatterer szinet
        WIN.fill(WHITE)
              
        # Kepek megjelenitese
        WIN.blit(hatter, (hatter_rect.x, hatter_rect.y))
        WIN.blit(level, (level_rect.x, level_rect.y))
        WIN.blit(auto1, (auto1_rect.x, auto1_rect.y))
        WIN.blit(auto2, (auto2_rect.x, auto2_rect.y))
        WIN.blit(auto3, (auto3_rect.x, auto3_rect.y))
        WIN.blit(beka, (beka_rect.x, beka_rect.y))
        
        #szoveg kiirasa
        WIN.blit(beka_szamlalo, (beka_szamlalo_rect.x, beka_szamlalo_rect.y))
        WIN.blit(elet_szamlalo, (elet_szamlalo_rect.x, elet_szamlalo_rect.y))
        WIN.blit(ido_szoveg, (ido_rect.x, ido_rect.y))
                              
                
        # Frissitjuk a teljes kepernyot, hogy ha valtozna valami akkor az megjelenjen
        pygame.display.update()
        
    # Lezarjuk az inicializalt funkciokat ,amit a pygame.init() letrehozott
    pygame.quit()

# Futtatjuk a fenti main fugvenyt, ha ezt a fajlt futtatjuk
if __name__ == '__main__':
    main()

