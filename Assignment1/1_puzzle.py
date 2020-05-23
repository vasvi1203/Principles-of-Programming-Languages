'''Solve the puzzle with a Python program: A man is walking down the village road with a tiger, a goat and a bundle of grass. Soon he arrives at the river bank where there is one tiny boat that can carry him and another animal or grass at a time. Here is the problem : Left alone, the tiger will eat the goat. And similarly, the goat will eat the grass bundle. How is he going to take all three across the river safely?'''

b1 = {"grass", "goat", "tiger"}
b2 = set()
case1 = {"grass", "goat"}
case2 = {"tiger", "goat"}
b = 1
while len(b1) != 0:
    if b == 1:              # farmer on bank 1
        if len(b1) == 3:    # all on bank 1
            obj = b1.pop()  # obj to be taken from bank 1 to bank 2
            
            if b1 != case1 and b1 != case2:     # tiger and grass on bank 1
                print("Farmer takes " + obj + " from bank1 to bank2")
                b2.add(obj)     # obj on bank 2
                b = 2
            else:
                b1.add(obj)     # if case1 or case2 occurs, obj not taken from bank 1 to bank 2
        else:
            obj = b1.pop()      # tiger and grass left on bank 1
            print("Farmer takes " + obj + " from bank1 to bank2")      # takes tiger or grass
            b2.add(obj)         
            b = 2
    else:
        if b2 == case1 or b2 == case2:      # tiger and goat or goat and grass on bank 2
            obj = b2.pop()                  # obj to be taken from bank 2 to bank 1
            print("Farmer takes " + obj + " from bank2 to bank1")
            b1.add(obj)         
        else:
            print("Farmer comes from bank2 to bank1")    

        b = 1
