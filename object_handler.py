from npc import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprites_path = 'resources/sprites/npc/'
        self.static_sprites_path = 'resources/sprites/static-sprites/'
        self.anim_sprites_path = 'resources/sprites/animated-sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 5.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprites_path + '/red-light/0.png', pos=(14.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprites_path + '/red-light/0.png', pos=(12.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprites_path + '/red-light/0.png', pos=(9.5, 7.5)))

        add_npc(SoldierNpc(game))
        add_npc(SoldierNpc(game, pos=(7, 4.5)))
        add_npc(SoldierNpc(game, pos=(11.5, 4.5)))
        add_npc(CacoDemonNpc(game))
        add_npc(CacoDemonNpc(game, pos=(7, 2.5)))
        add_npc(CyberDemonNpc(game))

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
