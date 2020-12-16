import pygame
from pygame.locals import *

pygame.init()


#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1600, 900), RESIZABLE)
#Nommer la page
pygame.display.set_caption("Menu jeu")
#Chargement et collage du fond
fond = pygame.image.load("1.png").convert()
fenetre.blit(fond,(0,0))
#Chargement et collage du bouton1
Bouton_1 = pygame.image.load("1.png").convert_alpha()
Bouton_1_pos = (540, 250)
fenetre.blit(Bouton_1, Bouton_1_pos)
#Chargement et collage du bouton2
Bouton2 = pygame.image.load("1.png").convert_alpha()
Bouton2_pos = (540,450)
fenetre.blit(Bouton2, Bouton2_pos)
#Chargement et collage du bouton_3
Bouton3 = pygame.image.load("1.png").convert_alpha()
Bouton3_pos = (540,650)
fenetre.blit(Bouton3, Bouton3_pos)
#Chargement et collage du text1
Text1_pos = (540, 250)
font = pygame.font.Font(None, 70)
Text1 = font.render("JOUER",1,(10,10,10))
fenetre.blit (Text1, Text1_pos)
#Chargement et collage du text2
Text2_pos = (540, 450)
font = pygame.font.Font(None, 70)
Text2 = font.render("OPTION",1,(10,10,10))
fenetre.blit (Text2, Text2_pos)
#Chargement et collage du text3
Text3_pos = (540, 650)
font = pygame.font.Font(None, 70)
Text3 = font.render("QUITTER",1,(10,10,10))
fenetre.blit (Text3, Text3_pos)


continuer = 1


while continuer:
    for event in pygame.event.get():    #Attente des événements
        if event.type == QUIT:
            continuer = 0


    #Rafraichissement
    pygame.display.flip()