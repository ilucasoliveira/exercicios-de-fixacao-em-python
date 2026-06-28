from abc import ABC, abstractmethod
from random import randint, choice

class Personagem(ABC):
    def __init__(self, nome, nivel, hp=200):
        self.nome = nome
        self.nivel = nivel
        self._hp = hp
        self.hp_max = hp
    
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, valor: int):
        self._hp = max(0, valor)
    
    def estar_vivo(self):
        return self._hp > 0
    
    def receber_dano(self, dano: int):
        new_hp = self.hp - dano
        self.hp = new_hp
        return self.hp
    
    @abstractmethod
    def atacar(self, alvo):
        pass
    
    def apresentar(self):
        return f"Nome: {self.nome}, Nível: {self.nivel}, HP: {self.hp}"

class Mago(Personagem):
    def __init__(self, nome, nivel, mana, poder_unico, hp=200):
        super().__init__(nome, nivel, hp)
        self.mana = mana
        self.poder_unico = poder_unico
    
    def atacar(self, alvo):
        dano = randint(20, 50)
        alvo.receber_dano(dano)
        self.mana -= randint(10, 12)
    
    def habilidade(self):
        return f"{self.nome} usou {self.poder_unico}!"
    
    def apresentar(self):
        return super().apresentar() + f", Mana: {self.mana}, Poder: {self.poder_unico}"

class Guerreiro(Personagem):
    def __init__(self, nome, nivel, forca, poder_unico, hp=200):
        super().__init__(nome, nivel, hp)
        self.forca = forca
        self.poder_unico = poder_unico
    
    def atacar(self, alvo):
        dano = randint(20, 40)
        alvo.receber_dano(dano)
        self.forca -= randint(6, 8)
    
    def habilidade(self):
        return f"{self.nome} usou {self.poder_unico}!"
    
    def apresentar(self):
        return super().apresentar() + f", Força: {self.forca}, Poder: {self.poder_unico}"

class Curandeiro(Personagem):
    def __init__(self, nome, nivel, mana, hp=200):
        super().__init__(nome, nivel, hp)
        self.mana = mana
    
    def atacar(self, alvo):
        dano = randint(10, 20)
        alvo.receber_dano(dano)
        self.mana -= randint(6,9)
    
    def curar(self, aliado):
        cura = randint(15, 30)
        if self.mana > 0:
            aliado.hp = min(aliado.hp + cura, aliado.hp_max)
            self.mana -= randint(15, 20)

class Batalha():
    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2
    
    def lutar(self):
        while any(p.estar_vivo() for p in self.time1) and any(p.estar_vivo() for p in self.time2):
            
            for p in self.time1:
                if p.estar_vivo():
                    vivos = [p for p in self.time2 if p.estar_vivo()]
                    alvo = choice(vivos)
                    p.atacar(alvo)
            
            for p in self.time2:
                if p.estar_vivo():
                    vivos = [p for p in self.time1 if p.estar_vivo()]
                    alvo = choice(vivos)
                    p.atacar(alvo)
        
        if any(p.estar_vivo() for p in self.time1):
            return "Parabéns, o Time 1 venceu a batalha!"
        else:
            return "Parabéns, o Time 2 venceu a batalha!"