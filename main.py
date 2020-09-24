'''


Metro 2033
Game


'''
from PIL import Image
print("Metro 2033")
print("The untold stories of Khan")

play = input("Press x to play>> ")


start = False

#Start button
if play == ("x"):
  start = True

#First "Scene"
if (start):
  print("I was in the metro again, I was lost, I need to find the nearest station")

metroMap1 = ["Follow the rail tracks", "Go above ground", "Swim through the sewers" ]


#Tells which map your are in
map1 = False
map2 = False
map3 = False






userInput1 = input("Follow the rail tracks, Go above ground, Swim through the sewers >>")

def metro(metroMap1):
  if userInput1 == (metroMap1[0]):
    print("\n I followed the trail, the only thing that you can hear are my footsteps. There is a legend that if you listen close enough you can hear the cries of souls telling you to go back. Up ahead you hear a bell, that is the same sound you hear if a station was opening a gate. I travelled further to figure out it is a live station with people! Hopefully they would let me in.")
    map1 = True
    map = Image.open('map1.jpg')
    map.show()
metro(metroMap1)




























'''


from random import choice
from random import randint
directions = ["north", "south", "east", "west"]
print("+---- Castle Adventure Game ----+")

def move(direction):
    keepgoing = True 
    if (answer == "n"):
      print("Moving north...")
    elif (answer == "s"):
      print("Moving south...")
    elif (answer == "e"):
      print("Moving east...")
    elif (answer == "w"):
      print("Moving west...")
    else:
      print("stopping")
      keepgoing = False 
    return keepgoing
keepgoing = True
inventory = []
def additem(item): 
    inventory.append(item)

def lookingAround():
  things = ["a cardboard box", "a staff", "a minimal wear stattrak krambit doppler from csgo", "a large glowing lightbulb" ]
  item = choice(things)
  print("You found", item)
  answer = input("Do you want to keep this item y/n >>>")
  if(answer == "y"):
      additem(item)
  print (inventory)
  return True
def dropitem():
    if(randint(0, 10) == 1):
      print ("You have dropped all of your items!")
      inventory.clear()
while(keepgoing):
    answer = input("Choose a direction: (n, s, e, w, l) >> ")
    if (answer == "l"):
      lookingAround()
    else:
      keepgoing = move(answer)
      dropitem()







'''