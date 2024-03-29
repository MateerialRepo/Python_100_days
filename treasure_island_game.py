# link to the flowchart https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# asci art from ascii.co.uk/art
print('''
  ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: .lcf/
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~
''')


print("Welcome to Treasure Island.\nYour mission is to find the missing Treasure")
direction = input("You are at a cross road. Do you go 'left' or 'right'? ").lower()
if direction == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    lake_choice = input("Type 'wait' to wait for a boat or 'swim' to swim across the lake. ")
    if lake_choice.lower() == "wait":
        print("You arrive at the island. You step of the boat and face a house with 3 doors")
        print("One is red, one is yellow and one is blue.")
        door_choice = input("Which of the colors do you choose? ").lower()
        if door_choice == "red":
            print("You are engulfed by fiery fire!!!\n")
            print("Game Over")
        elif door_choice == "blue":
            print("You are attacked by a swarm of bees!!!\n")
            print("Game Over")
        elif door_choice == "yellow":
            print("You found the treasure!!!")
            print("You win!!!")
        else:
            print("Game Over")

    else:
        print("You are attacked by crocodiles!!!!")
        print("Game Over")
else:
    print("Watch out!!!! You have fallen into a hole")
    print("Game Over")
