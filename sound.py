import pygame

class Sound:
    def __init__(self, game):
        self.game = game
        pygame.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pygame.mixer.Sound(self.path + 'shotgun.wav')
        self.npc_pain = pygame.mixer.Sound(self.path + 'npc-pain.wav')
        self.npc_death = pygame.mixer.Sound(self.path + 'npc-death.wav')
        self.npc_shot = pygame.mixer.Sound(self.path + 'npc-attack.wav')
        self.player_pain = pygame.mixer.Sound(self.path + 'player-pain.wav')
        self.theme = pygame.mixer.Sound(self.path + 'theme.mp3')
