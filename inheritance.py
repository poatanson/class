class Character:
  def __init__(self, name, hp, power):
    self.name = name
    self.hp = hp
    self.power = power
    
  def attack(self, other):
    print(f"{self.name}이(가) {other.name}을(를) 공격합니다")
    other.take_damage(self.power)
   
  def is_alive(self):
    return self.hp > 0
   
  def show_status(self):
    print(f"{self.name}의 상태: HP {self.hp}")
   
  def take_damage(self, damage):
    self.hp -= damage
    print(f"{self.name}이(가) {damage}의 피해를 입었습니다. 현재 HP: {self.hp}")
   
# Character 클래스를 상속받는 Player 클래스
class Player(Character):
  def __init__(self, name, hp, power):
    # super()는 부모 클래스(Character)의 __init__ 메소드를 호출함
    super().__init__(name, hp, power)
    # Player만의 추가 속성 (예: 마나)
    self.mana = 100
   
  # 메소드 오버라이딩(Method Overriding): 부모의 메소드를 재정의
  def show_status(self):
    print(f"플레이어 {self.name}의 상태: HP {self.hp}, MP {self.mana}")
   
# Character 클래스를 상속받는 Enemy 클래스
class Enemy(Character):
  def __init__(self, name, hp, power, bounty):
    super().__init__(name, hp, power)
    # Enemy만의 추가 속성 (예: 현상금)
    self.bounty = bounty
   
player = Player("용사", hp=200, power=15)
monster = Enemy("드래곤", hp=150, power=20, bounty=500)
   
player.show_status()
monster.show_status()
   
print("\n--- 전투 시작 ---")
player.attack(monster)
monster.attack(player)
   
print("\n--- 전투 후 상태 ---")
player.show_status()
monster.show_status()
