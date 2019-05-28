import pygame
import random
from os import path
from untitled0 import *

class Game:
    def __init(self):
        pass
    
    def new(self):
        # Resetar o jogo
       pass
        
    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.uptade()
            self.draw()
    
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
        self.screen.fill(WHITE)
        self.draw_text("Summoners", 48, BLACK, WIDTH/2, HEIGHT/4)
        self.draw_text("Pressione uma tela para jgoar", 22, BLACK, WIDTH/2, HEIGHT * 3/4)
        pygame.display.flip()
        self.wait_for_key()
    
    def show_go_screen(self):
        # Tela de game over / continue
        pass
    
    def wait_go_screen(self):
        waiting = True
        while waiting:
            self.clock.ticks(FPS) #ou 30
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False
    
g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
    
pygame.quit()
quit()