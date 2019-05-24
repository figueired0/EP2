import pygame
import random
from os import path
from Settings import WIDTH, HEIGHT, img_dir, snd_dir

class Game:
    def __init(self):
        # iniciar a tela do jogo
        # Inicialização do Pygame.
        pygame.init()
        pygame.mixer.init()
        
        # Tamanho da tela.
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        
        # Nome do jogo
        pygame.display.set_caption("Summoners")
        
        # Carrega todos os assets uma vez só e guarda em um dicionario
        assets = load_assets(img_dir,snd_dir)
        
        # Variável para o ajuste de velocidade
        self.clock = pygame.time.Clock()
        
        # Carrega o fundo do jogo
        background = assets["background_img"]
        background_rect = background.get_rect()
        
        # Carrega os sons do jogo
        pygame.mixer.music.load(path.join(snd_dir, 'Background_sound.ogg'))
        pygame.mixer.music.set_volume(0.4)
        
        
        
        self.running = True
    
    def new(self):
        # Resetar o jogo
        # Cria um grupo de todos os sprites e adiciona o personagem.
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player1)
        all_sprites.add(player2)

        # Cria um personagem. O construtor será chamado automaticamente.
        player1 = Player(assets['player1_img'])
        player2 = Player(assets['Player2_img'])
        player1.enemy = player2.rect
        player2.enemy = player1.rect
        
    def run(self):
        # Game loop
        pass
    
    def uptade(self):
        # Game loop - update
        pass
    
    def events(self):
        # Game loop - events
        pass
    
    def draw(self):
        # Game loop - draw
        pass
    
    def show_start_screen(self):
        # Tela de início do jogo
        pass
    
    def show_go_screen(self):
        # Tela de game over / continue
        pass
    
g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
    
pygame.quit()