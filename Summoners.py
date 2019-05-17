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

# Classe Jogador que representa o personagem
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, player_img):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        
        # Carregando a imagem do personagem.
        player_img = pygame.image.load(path.join(img_dir, "scooby.png")).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (100, 80))
        
        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        # self.rect.width = self.rect.width/2
        
        # Posição do personagem
        self.pos = vec(WIDTH /2, HEIGHT / 2)
        self.rect.center = (WIDTH / 2, HEIGHT /2)
        
        # Aceleração
        self.acc = vec(0, 0)
        
        # Velocidade
        self.vel = vec(0, 0)
        
        # Propriedades dos jogadores (Movimento)
        self.PLAYER_ACC = 1
        self.PLAYER_FRICTION = -0.12
        self.PLAYER_GRAV = 0.5
        
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
        self.pos += self.vel #+ 0.5 * self.acc
                
        # Mantem dentro da tela
        if self.pos.x > WIDTH - 50:
            self.pos.x = WIDTH - 50
        if self.pos.x < 50:
            self.pos.x = 50
        if self.pos.y > (HEIGHT - 40):
            self.pos.y = (HEIGHT - 40)
            self.vel.y = 0
        if self.pos.y == 0:
            self.pos.y = 0
            self.vel.y = 0
            
        self.rect.midbottom = self.pos
        
    def jump(self):
        # Personagem pula somente se estiver na plataforma
        if self.vel.y >= 0:
            self.vel.y = -20

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        
        # Construtor da classe pai (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((w, h))
        self.image.fill(WHITE)
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
        self.speedx = -20
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.centerx < 0:
            self.kill()
       
# Carrega todos os assets uma vez só           
def load_assets(img_dir, snd_dir):
    assets={}
    assets['player1_img'] = pygame.image.load(path.join(img_dir,'scooby.png')).convert()
    assets["background_img"] = pygame.image.load(path.join(img_dir,"Cenário.gif")).convert()
    assets['Player2_img'] = pygame.image.load(path.join(img_dir, 'scooby.png')).convert()
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
player1 = Player(assets['player1_img'])
player2 = Player(assets['Player2_img'])
player1.enemy = player2.rect
player2.enemy = player1.rect

# Cria um grupo de todos os sprites e adiciona o personagem.
all_sprites = pygame.sprite.Group()

all_sprites.add(player1)
all_sprites.add(player2)

# Cria um grupo de todos os sprites e adiciona uma plataforma.
platforms = pygame.sprite.Group()

# Cria um grupo de todos os sprites e adciona um bullet.
bullets = pygame.sprite.Group()

# Cria uma plataforma
p1 = Platform(0, HEIGHT - 40, WIDTH, 40)
all_sprites.add(p1)
platforms.add(p1)

p2 = Platform(WIDTH/2 - 10, HEIGHT - 110, 50, 50)
all_sprites.add(p2)
platforms.add(p2)

p3 = Platform(WIDTH/2 - 30, HEIGHT - 130, 50, 40)
all_sprites.add(p3)
platforms.add(p3)

#p3 = Platform(WIDTH/2 - 50, HEIGHT * 3 / 4, 50, 40)
#all_sprites.add(p3)
#platforms.add(p3)
#
#p4 = Platform(WIDTH/2 - 50, HEIGHT * 3 / 4, 50, 50)
#all_sprites.add(p4)
#platforms.add(p4)
#
#p5 = Platform(WIDTH/2 - 50, HEIGHT * 3 / 4, 50, 60)
#all_sprites.add(p5)
#platforms.add(p5)

# Comando para evitar travamentos.
try:
    
    # Loop principal.
    pygame.mixer.music.play(loops=-1)
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Define a gravidade
        player1.acc = vec(0 , player1.PLAYER_GRAV)
        player2.acc = vec(0 , player2.PLAYER_GRAV)
        
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
                    player1.jump()
                # Tiro
                if event.key == pygame.K_SPACE:
                        bullet = Bullet(player1.rect.centerx, player1.rect.top, assets["bullet_img"])
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        
                        
                # PLAYER 2
                # Pulo
                if event.key == pygame.K_w:
                    player2.jump()
                # Tiro
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
        hits1 = pygame.sprite.spritecollide(player1, platforms, False)
        hits2 = pygame.sprite.spritecollide(player2, platforms, False)
        if hits1:
            if player1.pos.y < hits1[0].rect.bottom:
            # Jogador 1 colide com a plataforma
                player1.pos.y = hits1[0].rect.top
                # jogar 1 se mantém na plataforma
                player1.vel.y = 0
            
        if hits2:
            if player1.pos.y < hits2[0].rect.bottom:
                # Jogador 2 colide com a plataforma
                player2.pos.y = hits2[0].rect.top
                # Jogador 2 se mantém na plataforma
                player2.vel.y = 0
        
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(WHITE)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()
    quit()