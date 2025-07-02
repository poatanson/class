class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp 
        self.power = power
    
    def attack(self, other):
        print(f"{self.name}가 {other.name}을(를) 공격합니다!")
        other.hp -= self.power
        
    def is_alive(self):
        return self.hp > 0
        
    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}")
        
player = Character("광전사", hp=100, power=10)
monster = Character("고블린", hp=30, power=5)

player.show_status()
monster.show_status()

player.attack(monster)

monster.show_status()
