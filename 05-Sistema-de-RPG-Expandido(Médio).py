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
        self.mana = max(0, self.mana - randint(10, 12))
        return f"{self.nome} atacou {alvo.nome} lhe causando {dano} de dano."
    
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
        self.forca = max(0, self.forca - randint(6, 8))
        return f"{self.nome} atacou {alvo.nome} lhe causando {dano} de dano."
    
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
        self.mana = max(0, self.mana - randint(6,9))
        return f"{self.nome} atacou {alvo.nome} lhe causando {dano} de dano."
    
    def curar(self, aliado):
        cura = randint(15, 30)
        if self.mana > 0:
            aliado.hp = min(aliado.hp + cura, aliado.hp_max)
            self.mana = max(0, self.mana - randint(15, 20))
        return f"{self.nome} curou {aliado.nome} em {cura}HP | {aliado.nome}: {aliado.hp}HP."

class Batalha():
    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2
    
    def config_luta(self,atacante1, atacante2):
        for p in atacante1:
            if isinstance(p, Curandeiro):
                precisa_curar = [a for a in atacante1 if a.hp < a.hp_max * 0.3 and a.estar_vivo()]
                if precisa_curar and p.estar_vivo():
                    aliado = choice(precisa_curar)
                    print(p.curar(aliado))
                elif p.estar_vivo():
                    vivos = [i for i in atacante2 if i.estar_vivo()]
                    if vivos:
                        alvo = choice(vivos)
                        print(p.atacar(alvo))
            else:
                if p.estar_vivo():
                    vivos = [i for i in atacante2 if i.estar_vivo()]
                    if vivos:
                        alvo = choice(vivos)
                        print(p.atacar(alvo))
    
    def lutar(self):
        while any(p.estar_vivo() for p in self.time1) and any(p.estar_vivo() for p in self.time2):
            self.config_luta(self.time1, self.time2)
            self.config_luta(self.time2, self.time1)
        
        if any(p.estar_vivo() for p in self.time1):
            return "Parabéns, o Time 1 venceu a batalha!"
        else:
            return "Parabéns, o Time 2 venceu a batalha!"

ahri = Mago("Ahri", 27, 200, "Raposa Espiritual")
katarina = Guerreiro("Katarina", 30, 100, "Tornado de Adagas")
lulu = Curandeiro("Lulu", 18, 200)

time1 = [ahri,katarina,lulu]

garen = Guerreiro("Garen", 45, 300, "Justiça Demaciana")
gangplank = Guerreiro("Gangplank", 50, 300, "Barragem de Canhão")
taric = Curandeiro("Taric", 51, 200)

time2= [garen,gangplank,taric]

batalha = Batalha(time1, time2)
print(batalha.lutar())