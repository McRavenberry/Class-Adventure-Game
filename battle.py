from os import system
from classes import Enemy
from random import randint
import time


def random_battle(player):
    system("clear")
    enemy = Enemy("Filler", 20, 5, 75, 100, 100, 3, 20)

    pf = True
    # block = False
    while player.health > 0 and enemy.health > 0:
      enemy_att = randint(1,4)
      if pf:
        while True:
          print(str(player.name) + " Health: " + str(player.health) + "/" +   str(player.max_health))
          print(str(enemy.name) + " Health: " + str(enemy.health) + "/" + str(enemy.max_health))
          print("""
          """)
    
          print("Attack [1]")
          print("Strong Attack [2]")
          print("Block [3]")
          print("Escape [4]")
    
          select = input("> ")
    
          if select == "1":
            print("Attack One")
            enemy.health -= 20
            # print("Player dealt " + str(20) + " to enemy!")
            break
            
          elif select == "2":
            print("Strong Attack")
            enemy.health -= 40
            # print("Player dealt " + str(40) + " to enemy!")
            input()
            break
            
          elif select == "3":
            print("Blocked")
            # block = True
            break
            
          elif select == "4":
            if enemy.health < 150:
              print("""
              """)
              print("You ran away...")
              print("End Battle code goes here")
              break
            else:
              print("You couldn't escape!")
              break
            
          # system("clear")
        
      else:
        if enemy_att == 1:
          # if block:
          #   player.health -= (enemy.damage/2)
          #   print("Enemy dealt " + str(enemy.damage/2) + " To Player")
          # else:
            player.health -= enemy.attack
            print("Enemy dealt " + str(enemy.attack) + " To Player")
          
        else:
          player.health -= 10
          print("Enemy dealt " + str(10) + " To Player")
          print("""
        """)
  
      input()
      system("clear")
      
      if pf:
        pf = False
      else:
        pf = True
  
    print("end battle")
    return player
