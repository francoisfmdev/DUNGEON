import pygame

# --- Constantes ---
TILE_SIZE = 32
MAP_WIDTH = 20
MAP_HEIGHT = 20
SCREEN_WIDTH = TILE_SIZE * MAP_WIDTH
SCREEN_HEIGHT = TILE_SIZE * MAP_HEIGHT

# Position du héros dans la grille
hero_h = 18
hero_w = 2

# --- Map 20x20 ---
# --- Map 20x20 corrigée ---
map_data = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1],
    [1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]



# --- Initialisation Pygame ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Déplacement du héros")

# --- Chargement des images ---
floor_img = pygame.image.load("./assets/WHITE.png").convert()
wall_img = pygame.image.load("./assets/GREY.png").convert()
hero_img = pygame.image.load("./assets/HERO.png").convert_alpha()
ball_img = pygame.image.load("./assets/ball.png").convert_alpha()  # <- convert_alpha pour gérer la transparence

# Redimensionnement
floor_img = pygame.transform.scale(floor_img, (TILE_SIZE, TILE_SIZE))
wall_img = pygame.transform.scale(wall_img, (TILE_SIZE, TILE_SIZE))
hero_img = pygame.transform.scale(hero_img, (TILE_SIZE, TILE_SIZE))
ball_img = pygame.transform.scale(ball_img, (TILE_SIZE, TILE_SIZE))

# --- Données des balles ---
balls = [(18, 7), (16, 9), (14, 14)]
nb_ball = 0  # --- AJOUT : compteur de balles ramassées

# --- Boucle principale ---
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion des touches
    keys = pygame.key.get_pressed()
    new_h, new_w = hero_h, hero_w

    if keys[pygame.K_UP]:
        new_h -= 1
    elif keys[pygame.K_DOWN]:
        new_h += 1
    elif keys[pygame.K_LEFT]:
        new_w -= 1
    elif keys[pygame.K_RIGHT]:
        new_w += 1

    # Vérifie les collisions (si la nouvelle case n'est pas un mur)
    if 0 <= new_h < MAP_HEIGHT and 0 <= new_w < MAP_WIDTH:
        if map_data[new_h][new_w] == 0:
            hero_h, hero_w = new_h, new_w

    # --- AJOUT : ramassage des balles ---
    if (hero_h, hero_w) in balls:
        balls.remove((hero_h, hero_w))
        nb_ball += 1
        print(f"Balle ramassée ! Total : {nb_ball}")

    # Affichage de la carte
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            pos = (x * TILE_SIZE, y * TILE_SIZE)
            tile = map_data[y][x]
            if tile == 1:
                screen.blit(wall_img, pos)
            else:
                screen.blit(floor_img, pos)

    # --- AJOUT : affichage des balles restantes ---
    for (ball_y, ball_x) in balls:
        screen.blit(ball_img, (ball_x * TILE_SIZE, ball_y * TILE_SIZE))

    # Affiche le héros
    hero_pos = (hero_w * TILE_SIZE, hero_h * TILE_SIZE)
    screen.blit(hero_img, hero_pos)

    # Affiche le héros
    hero_pos = (hero_w * TILE_SIZE, hero_h * TILE_SIZE)
    screen.blit(hero_img, hero_pos)

    # --- Affichage du score ---
    font = pygame.font.Font(None, 28)
    text_surface = font.render(f"Balles : {nb_ball}", True, (0, 0, 0))
    screen.blit(text_surface, (10, 10))

    pygame.display.flip() # Affiche le héros
    hero_pos = (hero_w * TILE_SIZE, hero_h * TILE_SIZE)
    screen.blit(hero_img, hero_pos)

    # Affichage du score
    font = pygame.font.Font(None, 28)
    text_surface = font.render(f"Balles : {nb_ball}", True, (0, 0, 0))
    screen.blit(text_surface, (10, 10))

    # --- Condition de victoire ---
    if nb_ball == 3 and (hero_h, hero_w) == (0, 18):
        win_text = font.render("Vous avez gagné !", True, (0, 255, 0))
        screen.blit(win_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20))
        pygame.display.flip()
        pygame.time.delay(3000)  # Attente de 3 secondes
        pygame.quit()
        exit()

    pygame.display.flip()
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
