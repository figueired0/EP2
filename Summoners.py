# Importando as bibliotecas necessárias.
import pygame
from os import path
vec = pygame.math.Vector2

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

# Dados gerais do jogo.
WIDTH = 1278 # Largura da tela
HEIGHT = 718 # Altura da tela
FPS = 60 # Frames por segundo


# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Função Barra do Escudo
def draw_shield_bar(surf, x, y, pct): # (Superfície, posição x, posição y, porcentagem)
    if pct < 0:
        pct = 0
    # Tamanho da barra:
    BAR_LENGHT = 100
    BAR_HEIGHT = 10
    # O que enche a barra:
    fill = (pct/100)*BAR_LENGHT
    outline_rect = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

# Classe Jogador que representa o personagem
class Player1(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, player_img):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        
        # Carregando a imagem do personagem.
        player_img = pygame.image.load(path.join(img_dir, "scooby_esquerda.png")).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (100, 80))
        
        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        # self.rect.width = self.rect.width/2
        
        # Posição do personagem
        self.pos = vec(3.5 * WIDTH/6, HEIGHT / 2)
        self.rect.center = (WIDTH / 2, HEIGHT /2)
        
        # Aceleração
        self.acc = vec(0, 0)
        
        # Velocidade
        self.vel = vec(0, 0)
        
        # Escudo
        self.shield = 100
        
        # Tempo entre os tiros
        self.shoot_delay = 500
        self.last_shot = pygame.time.get_ticks()
        
        # Propriedades dos jogadores (Movimento)
        self.PLAYER_ACC = 1
        self.PLAYER_FRICTION = -0.12
        self.PLAYER_GRAV = 1.5
        self.PLAYER_JUMP = 20
        self.JUMPING1 = False
        
    # Metodo que atualiza a posição do boneco
    def update(self):
        # Gerando a graviade.
        self.acc = vec(0 , self.PLAYER_GRAV)
        
        # Definindo as teclas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -self.PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x = self.PLAYER_ACC
            
        
        # Aplicando a fricção ao movimento
        self.acc.x += self.vel.x * self.PLAYER_FRICTION
        
        # Detalhes da movimentação
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
                
        # Mantem dentro da tela
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH 
        if self.pos.x < 50:
            self.pos.x = 50
        if self.pos.y > (HEIGHT):
            self.pos.y = (HEIGHT )
            self.vel.y = 0
        if self.pos.y == 0:
            self.pos.y = 0
            self.vel.y = 0
            
        self.rect.midbottom = self.pos
        
    def jump(self):
        # Personagem pula somente se estiver na plataforma
        if self.vel.y >= 0:
            self.vel.y = -self.PLAYER_JUMP
    
    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
        bullet = Bullet(self.rect.centerx, self.rect.top, assets['bullet_img'])
        all_sprites.add(bullet)
        bullets1.add(bullet)

class Player2(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, player_img):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        
        # Carregando a imagem do personagem.
        player_img = pygame.image.load(path.join(img_dir, "scooby_direita.png")).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (100, 80))
        
        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        # self.rect.width = self.rect.width/2
        
        # Posição do personagem
        self.pos = vec(2*WIDTH /6, HEIGHT / 2)
        self.rect.center = (WIDTH / 2, HEIGHT /2)
        
        # Aceleração
        self.acc = vec(0, 0)
        
        # Velocidade
        self.vel = vec(0, 0)
        
        # Escudo
        self.shield = 100
        
        # Tempo entre os tiros
        self.shoot_delay = 500
        self.last_shot = pygame.time.get_ticks()
        
        # Propriedades dos jogadores (Movimento)
        self.PLAYER_ACC = 1
        self.PLAYER_FRICTION = -0.12
        self.PLAYER_GRAV = 1.5
        self.PLAYER_JUMP = 20
        self.JUMPING2 = False
        
    # Metodo que atualiza a posição do boneco
    def update(self):
        # Gerando a graviade.
        self.acc = vec(0 , self.PLAYER_GRAV)
        
        # Definindo as teclas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.acc.x = -self.PLAYER_ACC
        if keys[pygame.K_d]:
            self.acc.x = self.PLAYER_ACC
        
        # Aplicando a fricção ao movimento
        self.acc.x += self.vel.x * self.PLAYER_FRICTION
        
        # Detalhes da movimentação
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
                
        # Mantem dentro da tela
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 50:
            self.pos.x = 50
        if self.pos.y > (HEIGHT):
            self.pos.y = (HEIGHT)
            self.vel.y = 0
        if self.pos.y == 0:
            self.pos.y = 0
            self.vel.y = 0
            
        self.rect.midbottom = self.pos
        
    def jump(self):        
        # Personagem pula somente se estiver na plataforma
        if self.vel.y >= 0:
            self.vel.y = -self.PLAYER_JUMP
            
    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
        bullet = Bullet(self.rect.centerx, self.rect.top, assets['bullet_img'])
        all_sprites.add(bullet)
        bullets2.add(bullet)
        
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        
        # Construtor da classe pai (Sprite)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
#        self.image.set_colorkey(BLACK)
        self.rect = self. image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Bullet(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y, bullet_img):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = bullet_img
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y + 35
        self.rect.centerx = x - 35
        self.speedx = -10
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.centerx < 0:
            self.kill()
       
# Carrega todos os assets uma vez só           
def load_assets(img_dir, snd_dir):
    assets={}
    assets['player1_img'] = pygame.image.load(path.join(img_dir,'scooby_esquerda.png')).convert()
    assets["background_img"] = pygame.image.load(path.join(img_dir,"Cenário.gif")).convert()
    assets['Player2_img'] = pygame.image.load(path.join(img_dir, 'scooby_direita.png')).convert()
    assets['bullet_img'] = pygame.image.load(path.join(img_dir,'laserRed16.png')).convert()
    return assets


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Summoners")

# Carrega todos os assets uma vez só e guarda em um dicionario
assets = load_assets(img_dir,snd_dir)

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = assets["background_img"]
background_rect = background.get_rect()

# Carrega os sons do jogo
pygame.mixer.music.load(path.join(snd_dir, 'Background_sound.ogg'))
pygame.mixer.music.set_volume(0.4)


# Cria um personagem. O construtor será chamado automaticamente.
player1 = Player1(assets['player1_img'])
player2 = Player2(assets['Player2_img'])
player1.enemy = player2.rect
player2.enemy = player1.rect

# Cria um grupo de todos os sprites e adiciona o personagem.
all_sprites = pygame.sprite.Group()

all_sprites.add(player1)
all_sprites.add(player2)

# Cria um grupo de todos os sprites e adiciona uma plataforma.
platforms = pygame.sprite.Group()

# Cria um grupo de todos os sprites e adciona um bullet.
bullets1 = pygame.sprite.Group()
bullets2 = pygame.sprite.Group()

# Cria uma lista de plataforma plataforma
lista_de_plataforma = [(WIDTH/2 - 58, HEIGHT - 20, 40, 50),
                       (WIDTH/2 - 10, HEIGHT - 115, 50, 50),
                       (WIDTH/2 - 85, HEIGHT - 140, 50, 40),
                       (WIDTH/2 - 145, HEIGHT - 180, 50, 40),
                       (WIDTH/2 - 215, HEIGHT - 200, 50, 50),
                       (WIDTH/2 - 270, HEIGHT - 235, 50, 60),
                       (WIDTH/2 - 240, HEIGHT - 260, 30, 20),
                       (WIDTH/2 - 210, HEIGHT - 315, 320, 20),
                       (WIDTH/2 + 15, HEIGHT - 150, 65, 20),
                       (WIDTH/2 + 55, HEIGHT - 90, 55, 30),
                       (WIDTH/2 + 150, HEIGHT - 85, 55, 20),
                       (WIDTH/2 + 220, HEIGHT - 230, 55, 20),
                       (WIDTH/2 + 270, HEIGHT - 250, 55, 20),
                       (WIDTH/2 + 190, HEIGHT - 225, 20, 20),
                       (WIDTH/2 + 225, HEIGHT - 295, 20, 20),
                       (WIDTH/2 + 210, HEIGHT - 340, 30, 20),
                       (WIDTH/2 + 290, HEIGHT - 295, 40, 20),
                       (WIDTH/2 - 400, HEIGHT - 115, 90, 20),
                       (WIDTH/2 + 160, HEIGHT - 90, 30, 20),
                       (WIDTH/2 - 460, HEIGHT - 65, 85, 20),
                       (WIDTH/2 - 500, HEIGHT - 105, 45, 20),
                       (WIDTH/2 - 450, HEIGHT - 200, 40, 20),
                       (WIDTH/2 - 365, HEIGHT - 380, 60, 20),
                       (WIDTH/2 - 365, HEIGHT - 440, 40, 20),
                       (WIDTH/2 - 315, HEIGHT - 410, 20, 20),
                       (WIDTH/2 + 60, HEIGHT - 420, 60, 20),
                       (WIDTH/2 + 20, HEIGHT - 15, 130, 50),
                       (WIDTH/2 + 100, HEIGHT - 30, 80, 50),
                       (WIDTH/2 + 20, HEIGHT - 40, 70, 20),
                       (WIDTH/2 - 340, HEIGHT - 35, 60, 50),
                       (WIDTH/2 - 275, HEIGHT - 25, 20, 50),
                       (WIDTH/2 - 250, HEIGHT - 50, 70, 30),
                       (WIDTH/2 - 230, HEIGHT - 55, 30, 30),
                       (WIDTH/2 - 180, HEIGHT - 30, 65, 50),
                       (WIDTH/2 - 480, HEIGHT - 10, 70, 50)]
for plat in lista_de_plataforma:
    # Adicionando elemento da lista como uma plataforma
    p = Platform(*plat)
    # Adicionando cada plataforma no sprites e no grupo platforms
    all_sprites.add(p)
    platforms.add(p)
    
# Comando para evitar travamentos.
try:
    
    # Loop principal.
    pygame.mixer.music.play(loops=-1)
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                running = False
            
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # PLAYER 1
                # Pulo
                if event.key == pygame.K_UP:
                    if not player1.JUMPING1:
                        player1.JUMPING1 = True
                        player1.jump()
                if event.key == pygame.K_m:
                    player1.shoot()
                             
                # PLAYER 2
                # Pulo
                if event.key == pygame.K_w:
                    if not player2.JUMPING2:
                        player2.JUMPING2 = True
                        player2.jump()
                if event.key == pygame.K_f:
                    player2.shoot()
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
        if player1.pos.y or player2.pos.y >0:
            hits1 = pygame.sprite.spritecollide(player1, platforms, False)
            hits2 = pygame.sprite.spritecollide(player2, platforms, False)
            
            # Criando hit para o Tiro
            hits3 = pygame.sprite.spritecollide(player2, bullets1, True)
            hits4 = pygame.sprite.spritecollide(player1, bullets2, True)
            
            if hits1:
                if player1.pos.y < hits1[0].rect.bottom:
                # Jogador 1 colide com a plataforma
                    player1.pos.y = hits1[0].rect.top
                    # jogar 1 se mantém na plataforma
                    player1.vel.y = 0
                    player1.JUMPING1 = False
                
            if hits2:
                if player2.pos.y < hits2[0].rect.bottom:
                    # Jogador 2 colide com a plataforma
                    player2.pos.y = hits2[0].rect.top
                    # Jogador 2 se mantém na plataforma
                    player2.vel.y = 0
                    player2.JUMPING2 = False
                    
            for hits in hits3:
                player2.shield -= 25
                if player2.shield <= 0:
                    running = True
            for hits in hits4:
                player1.shield -= 25
                if player1.shield <= 0:
                    running = True
        
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(WHITE)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Desenha barra de escudo do player 1
        draw_shield_bar(screen, WIDTH - 105, 5, player1.shield)
        
        # Desenha barra de escudo do player 2
        draw_shield_bar(screen, 5, 5, player2.shield)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()
    quit()