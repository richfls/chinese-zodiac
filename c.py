year = int(input("what year were you born"))
num = year
if year%2 == 0:
    print("Yang ")
    year -= 4
    year%=10
    year/=2

    num-=4
    num%=12

    if year <= 0:
        print("WOOD ")
    elif year <= 1:
        print("FIRE ")
    elif year <= 2:
        print("EARTH ")
    elif year <= 3:
        print("METAL ")
    elif year <= 4:
        print("WATER ")

    if num <= 0:
        print("Rat ")
    elif num <= 1:
        print("Ox ")
    elif num <= 2:
        print("Tiger ")
    elif num <= 3:
        print("Rabbit ")
    elif num <= 4:
        print("Dragon ")
    elif num <= 5:
        print("Snake ")
    elif num <= 6:
        print("Horse ")
    elif num <= 7:
        print("Goat ")
    elif num <= 8:
        print("Monkey ")
    elif num <= 9:
        print("Rooster ")
    elif num <= 10:
        print("Dog ")
    elif num <= 11:
        print("Pig ")

else:
    print("Yin ")
    year -= 4
    year%=10
    year/=2

    num-=4
    num%=12

    if year <= 0:
        print("WOOD ")
    elif year <= 1:
        print("FIRE ")
    elif year <= 2:
        print("EARTH ")
    elif year <= 3:
        print("METAL ")
    elif year <= 4:
        print("WATER ")

    if num <= 0:
        print("Rat ")
    elif num <= 1:
        print("Ox ")
    elif num <= 2:
        print("Tiger ")
    elif num <= 3:
        print("Rabbit ")
    elif num <= 4:
        print("Dragon ")
    elif num <= 5:
        print("Snake ")
    elif num <= 6:
        print("Horse ")
    elif num <= 7:
        print("Goat ")
    elif num <= 8:
        print("Monkey ")
    elif num <= 9:
        print("Rooster ")
    elif num <= 10:
        print("Dog ")
    elif num <= 11:
        print("Pig ")
