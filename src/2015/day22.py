from collections import namedtuple
from functools import partial
from itertools import product
from math import ceil


class Actor:

    def __init__(self, hp, mp, ar=0, dmg=0, verbose=False):
        self.hp = hp
        self.mp = mp
        self.ar = ar
        self.dmg = dmg
        self.verbose = verbose
        self.effects = []

    def attack(self, target):
        target.hp -= max(self.dmg - target.ar, 1)
        if self.verbose:
            print(f'Attacking {target.__class__.__name__} for {max(self.dmg - target.ar, 1)} dmg')

    def resolve_effects(self):
        for effect in self.effects:
            effect.run()
        self.effects = [effect for effect in self.effects if effect.lifetime > 0]

    def __str__(self):
        return f'{self.__class__.__name__}: HP:{self.hp}, MP:{self.mp}, AR:{self.ar}, DMG: {self.dmg} \n  Active Effects: {self.effects}'


class Boss(Actor):
    pass


class Player(Actor):
    def __init__(self, hp, mp, ar=0, dmg=0, verbose=False, seed=None):
        super().__init__(hp,mp,ar,dmg,verbose=verbose)
        self.seed = seed
        self.mp_spent = 0
        self.spells = [self.mm, self.drain, self.shield, self.poison, self.recharge]

    def cast_spell(self, target):
        if self.seed:
            if self.verbose:
                print(f'Casting: {self.spells[int(self.seed[0])].__name__}')
            result = self.spells[int(self.seed[0])](target)
            self.seed = self.seed[1:]
            if result == 1:
                return 1
        else:
            return 1

    def attack(self, target):
        return self.cast_spell(target)

    def mm(self, target):
        self.mp -= 53
        self.mp_spent += 53
        if self.mp <= 0:
            return 1
        target.hp -= 4

    def drain(self, target):
        self.mp -= 73
        self.mp_spent += 73
        if self.mp <= 0:
            return 1
        target.hp -= 2
        self.hp += 2

    def shield(self, target):
        if any(ef.name=='shielded' for ef in self.effects):
            return 1

        self.mp -= 113
        self.mp_spent += 113
        if self.mp <= 0:
            return 1

        def shielded_setup(self):
            self.prebuff_ar = self.ar

        def shielded_teardown(self):
            self.ar = self.prebuff_ar

        def shielded(self):
            self.ar = self.prebuff_ar + 7

        effect = Effect(6,
                        partial(shielded, self),
                        setup=partial(shielded_setup, self),
                        teardown=partial(shielded_teardown, self),
                        name="shielded")
        self.effects.append(effect)

    def poison(self, target):
        if any(ef.name=='poisoned' for ef in target.effects):
            return 1
        self.mp -= 173
        self.mp_spent += 173
        if self.mp <= 0:
            return 1

        def poisoned(target):
            target.hp -= 3

        effect = Effect(6, partial(poisoned, target), name="poisoned")
        target.effects.append(effect)

    def recharge(self, target):
        if any(ef.name=='recharging' for ef in self.effects):
            return 1
        self.mp -= 229
        self.mp_spent += 229
        if self.mp <= 0:
            return 1

        def recharging(self):
            self.mp += 101

        effect = Effect(5, partial(recharging, self), name="recharging")
        self.effects.append(effect)

class Effect:

    def __init__(self, lifetime, executable, setup=None, teardown=None, name=None):
        self.name = name
        self.executable = executable
        self.teardown = teardown
        self.lifetime = lifetime
        if setup:
           setup()

    def run(self):
        if self.lifetime > 1:
            self.lifetime -= 1
            self.executable()
        elif self.lifetime == 1:
            self.lifetime -= 1
            self.executable()
            if self.teardown: self.teardown()
        else:
            pass

    def __str__(self):
        return f'<{self.name} duration: {self.lifetime}>'

    def __repr__(self):
        return f'<{self.name} duration: {self.lifetime}>'


class GameState:

    def __init__(self, seed, verbose=None, hardmode=False):
        self.seed = seed
        self.player = Player(50, 500, 0, 0, seed=seed, verbose=verbose)
        self.boss = Boss(58, 1, 0, 9, verbose=verbose)
        self.actors = [self.player, self.boss]
        self.verbose = verbose
        self.hardmode = hardmode

    def print_gameover(self, code):
        if code == 1:
            print(f'Gameover, boss won')
        else:
            print(f'Gameover, player won, spent {self.player.mp_spent}')


    def run_game(self):
        attacker = self.player
        defender = self.boss

        while True:
            if self.verbose:
                print(f"\n--- {attacker.__class__.__name__}'s turn ---")
                print(f'{attacker}')
            gameover = self.do_turn(attacker, defender)
            if gameover:
                break
            attacker, defender = defender, attacker

        if self.verbose:
            self.print_gameover(gameover)
        if gameover == 2:
            return self.player.mp_spent


    def check_game_over(self):
        if self.player.hp <= 0 or self.player.mp <= 0:
            return 1
        if self.boss.hp <=0:
            return 2
        return 0

    def do_turn(self, actor1, actor2):
        if self.hardmode:
            if actor1 == self.player:
                self.player.hp -= 1
                gameover = self.check_game_over()
                if gameover:
                    return gameover

        self.player.resolve_effects()
        gameover = self.check_game_over()
        if gameover:
            return gameover

        self.boss.resolve_effects()
        gameover = self.check_game_over()
        if gameover:
            return gameover

        invalid_state = actor1.attack(actor2)
        if invalid_state:
            return 1
        gameover = self.check_game_over()
        if gameover:
            return gameover

#wins = []
#for moves in range(9,10):
#    seeds = product([0,1,2,3,4],repeat=moves)
#    for seed in seeds:
#        game = GameState(seed = ''.join([str(s) for s in seed]))
#        result = game.run_game()
#        if result:
#            wins.append((result,seed))
#print(min(wins))
#
#wins = []
#for moves in range(9,10):
#    seeds = product([0,1,2,3,4],repeat=moves)
#    for seed in seeds:
#        game = GameState(seed = ''.join([str(s) for s in seed]), hardmode=True)
#        result = game.run_game()
#        if result:
#            wins.append((result,seed))
#print(min(wins))

game = GameState(seed = '342342300', verbose=True)
game.run_game()