# ---Snakes and Ladder---

# Function definition for Ladder
def ladders(i):
    if i == 4:
        i=14
        return i
    elif i == 9:
        i=31
        return i
    elif i == 20:
        i=38
        return i
    elif i == 28:
        i=84
        return i
    elif i == 40:
        i=59
        return i
    elif i == 51:
        i=67
        return i
    elif i == 63:
        i=81
        return i
    elif i == 71:
        i=91
        return i
    else:
        return i

# Function definition for Snakes
def snakes(i):
    if i == 17:
        i=7
        return i
    elif i == 54:
        i=34
        return i
    elif i == 62:
        i=19
        return i
    elif i == 64:
        i=60
        return i
    elif i == 87:
        i=24
        return i
    elif i == 93:
        i=73
        return i
    elif i == 95:
        i=75
        return i
    elif i == 99:
        i=78
        return i
    else:
        return i

# Function definition for Player 1
def Player1(i):
    print("Player 1:")
    val=random.randint(1,6)
    print("Dice shows:{0}".format(val))
    i=i+val
    print("Possible position:{0}".format(i))
    if i > 100:
        i=i-val
        print("New position:{0}\n".format(i))
    else:
        i=ladders(i)
        i=snakes(i)
        print("New position:{0}\n".format(i))
    if i == 100:
        w = 1
        print("Player 1 won")
        exit()
    else:
        return i

#Function Definition for Player 2
def Player2(j):
    print("Player 2:")
    val=random.randint(1,6)
    print("Dice shows:{0}".format(val))
    j=j+val
    print("Possible position:{0}".format(j))
    if j > 100:
        j=j-val
        print("New position:{0}\n".format(j))
    else:
        j=ladders(j)
        j=snakes(j)
        print("New position:{0}\n".format(j))
    if j == 100:
        w = 1
        print("Player 2 won")
        exit()
    else:
        return j

# Main Function
i=1
j=1
w=0
print("\n---Welcome To Snakes and Ladders---\n")
print("Initial position: 1 \n")
import random
while w==0:
    i=Player1(i)
    j=Player2(j)
