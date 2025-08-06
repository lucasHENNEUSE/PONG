import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (150, 0, 255)
RED = (255, 250, 0)

# Dimensions de l'écran
WIDTH = 800 # largeur de la fenêtre
HEIGHT = 600 # longueur de la fenêtre

# Création de la fenêtre du jeu
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # création de la fenêtre avec screen = écran
pygame.display.set_caption('Pong') # création du titre de la fenêtre

# Vitesse du jeu
FPS = 75 # configuration de la vitesse du jeu qui représente 60 image par seconde
clock = pygame.time.Clock() # la fonction clock permet de mesurer le temps écoulé en seconde, puis 'pygame.time.clock()' permet de contrôler cette fréquence d'images

# Classe pour la raquette
class Paddle: # représente l'objet ' une raquette'
    def __init__(self, x, y, width, height, color): #la méthode __init__ permet de construire l'objet et self désigne la position de la raquette
        self.rect = pygame.Rect(x, y, width, height)# self.rect est un attribut qui représente la raquette sous forme d'un objet de type RECT de la bibliothéque pygame
        #pygame.Rect(x,y,width,height) crée un rectangle avec la position dans le jeux en 2D
        self.color = color # annonce la varible de la couleur
        self.speed = 5 # définit la vitesse de la raquette

# définit le movement de la raquette
    def move_up(self): # déplacement de la raquette vers le haut
        if self.rect.top > 0: # Vérifie si le bord supérieur de l'objet (self.rect.top) est au-dessus du bord supérieur de l'écran (qui est à la position 0). Si c'est le cas, l'objet peut se déplacer vers le haut.
            self.rect.y -= self.speed # Si la condition est remplie, la position de l'objet est modifiée en diminuant la valeur de y de self.speed. Cela déplace l'objet vers le haut.

    def move_down(self): # déplacement de la raquette vers le bas
        if self.rect.bottom < HEIGHT: #Vérifie si le bord inférieur de l'objet (self.rect.bottom) est inférieur à la hauteur de l'écran (HEIGHT). Si l'objet n'est pas encore au bas de l'écran, il peut se déplacer vers le bas.
            self.rect.y += self.speed #Si la condition est remplie, la position de l'objet est modifiée en augmentant la valeur de y de self.speed, ce qui déplace l'objet vers le bas.


    def draw(self):# cette méthode sert à dessiner l'objet à l'écran
        pygame.draw.rect(screen, self.color, self.rect)# utilisation de la fonction pour dessiner un rectangle à l'écran, la couleur, sa dimensions et position

# Classe pour la balle
class Ball: # représente l'objet 'une balle'
    def __init__(self, x, y, radius, color): # permet de construire la balle
# Paramètres de constructeur de la balle
        self.x = x # position horizontale de la balle
        self.y = y # position verticale de la balle
        self.radius = radius # le rayon de la balle (soit sa taille)
        self.color = color # la couleur de la balle
        self.speed_x = 5 # la vitesse de la balle à l'horizontale
        self.speed_y = 5 # la vitesse de la balle à la verticale

    def move(self):
        self.x += self.speed_x # modification de la position de l'objet sur l'axe X
        self.y += self.speed_y # modicfication de la position de l'objet sur l'axe Y

# ce code permet à la balle de rebondir l'orsqu'il atteint le bord supérieur ou inférieur de l'écran
    def bounce(self):
        if self.y <= 0 or self.y >= HEIGHT - self.radius: # cela signifie que l'objet a atteint le bord supérieur de l'écran
            self.speed_y = -self.speed_y # cela signifie que la balle a atteind le bord inférieur de l'écran

# la méthode reset qui permet de réinitialiser la balle à sa position de départ aprés un point marqué
    def reset(self):
        self.x = WIDTH // 2 # place la balle au centre de l'écran pour la variable WIDTH, ::2 permet de diviser la largeur par 2 pour obtenir la position centrale horizontale
        self.y = HEIGHT // 2
        self.speed_x = -self.speed_x # cela inverse la vitesse de l'objet sur l'axe x (horizontal) l'objet se déplace vers la droite aprés reset() il se déplace vers la gauche
        self.speed_y = 5 # définit une vitesse verticale initiale de l'objet sur l'axe des Y la vistesse 5 unités

    def draw(self): # la méthode draw() sert à dessiner un cercle soit la balle
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius) # reprend les variables

# Création des objets raquettes et balle
player1 = Paddle(30, HEIGHT // 2 - 50, 20, 100, RED) #30 repréente la position x de la raquette ( à gauche), height//2-50 la position y de la raquette soit centrée verticalement dans la fenêtre, 20 la largeur de la raquette,100 se hauteur, RED la couleur
player2 = Paddle(WIDTH - 50, HEIGHT // 2 - 50, 20, 100, RED)
ball = Ball(WIDTH // 2, HEIGHT // 2, 15, WHITE)# WIDTH//2 la position x de la balle soir au centre horizontale, HEIGHT//2 la position y soit au centre vertical, 15 le rayon de la balle, WHITE la couleur

# Fonction de gestion du score
font = pygame.font.SysFont('Arial', 30)# représente la police de caractères et sa taille de 30 pixels
# fonction qui initialisent les scores des deux joueurs à zéro au début du jeu
score1 = 0
score2 = 0

# fonction pour afficher le score
def display_score():
    score_text = font.render(f'{score1} - {score2}', True, WHITE)# font.render() méthode pour créer une image du texte à afficher, true white permet de donner une écriture blanche et net
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))# définit la position du texte, elle calcule la position horizontale et l'axe vertical est fixé à 20 pixels

# Boucle principale du jeu
while True:# définit la boucle infinie
    screen.fill(BLACK)# définit la boucle pour affgicher l'écran en Noir
    
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Déplacements des raquettes
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        player1.move_up()
    if keys[pygame.K_s]:
        player1.move_down()
    if keys[pygame.K_UP]:
        player2.move_up()
    if keys[pygame.K_DOWN]:
        player2.move_down()

    # Déplacement et rebond de la balle
    ball.move()
    ball.bounce()

    # Vérification des collisions avec les raquettes
    if player1.rect.colliderect(pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2)) or \
       player2.rect.colliderect(pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2)):
        ball.speed_x = -ball.speed_x

    # Vérification si un joueur marque
    if ball.x <= 0:
        score2 += 1
        ball.reset()
    elif ball.x >= WIDTH:
        score1 += 1
        ball.reset()

    # Affichage des éléments à l'écran
    player1.draw()
    player2.draw()
    ball.draw()
    display_score()

    # Mise à jour de l'écran
    pygame.display.flip()

    # Contrôle du FPS
    clock.tick(FPS)
