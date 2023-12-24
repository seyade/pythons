from random import randint
# import random
import openai

my_name = "Sey"

def show_name(name):
  print(name)

show_name(my_name)

mangas = ["Dragon Ball Z", "One Piece", "Naruto", "Hajime no Ippo", "Attack of The Titans"]

mangas.append("Dragon Ball GT")

for manga in mangas:
  print(manga)

print(mangas[:3])

# file: fighter.py
class Fighter:
  def __init__(self, name):
    self.name = name

  hp = 1

  def attack(self):
    self.hp = self.hp + 1
    print(self.name + " power increases")

# file: bear.py
class Bear:
  def __init__(self, name, type_of_Bear):
    self.name = name
    self.type_of_Bear = type_of_Bear
  
  hp = 150

  def roar(self):
    print(self.name + " roars...")
  
  def eat(self):
    print(self.name + " eats fish...")

winnie_the_poo = Bear("Winnie The Poo", "Polar bear")
winnie_the_poo.roar()
winnie_the_poo.eat()

fighter = Fighter("Goku")
fighter.hp = randint(1, 200)

fight_status = "Draw"

print(fighter.name + " HP: ", fighter.hp)

if (fighter.hp > winnie_the_poo.hp):
  fighter.attack()
  print(fighter.name + " win...")
  fight_status = "Win"
elif(fighter.hp == winnie_the_poo.hp):
  fighter.attack()
  print(fighter.name + " need more training...")
  fight_status = "Loose"
else:
  fighter.attack()
  print(fighter.name + " draws...")
  fight_status = "Draw"

if (fight_status == "Win"):
  print("Now go and get some food")

def fighting(animal):
  print("The " + animal " attacks you")
  if (animal > 100):
    return 105

fighting("Bear")
fighting("Eagle")
fighting("Snake")
fighting("Doplhin")




