class Pokemon:
    def __init__(self, nome, ataque, defesa, velocidade, hp):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.hp = hp

    def copy(self):
        return Pokemon(
            self.nome,
            self.ataque,
            self.defesa,
            self.velocidade,
            self.hp
        )