# Β© The owner of this code is Mehmet GΓΌdΓΌk.
# Β© Licensed with GPL-3.0 License

from random import choice, shuffle
from time import sleep
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
        
clear()     


try:
    print("\n")
    print(" π  -  π ".center(100,"*"))
    print(" [1] [2] [3] [4] [5] ".center(100,"*"))
    game_speed = int(input("- π Game speed : "))
    game_speed = 5 - game_speed + 1
    if (game_speed != 1) and (game_speed != 2) and (game_speed != 3) and (game_speed != 4) and (game_speed != 5):
        raise ValueError
except ValueError:
    game_speed = 1


game_count = 1
changed = []
notchanged = []


while True:
    clear()
    print(" ")
    game_title = f" GAME : {game_count} ".center(26, "β¬")
    print(game_title)
    print(" ")
    game_count += 1


    objects = ["π","π","π"]
    shuffle(objects)
    selected_one = choice(objects)
    del objects[objects.index(selected_one)]
    selected_two = choice(objects)
    del objects[objects.index(selected_two)]
    selected_three = choice(objects)
    del objects[objects.index(selected_three)]


    doors = ["DOOR1", "DOOR2", "DOOR3"]
    symbols = [selected_one, selected_two, selected_three]
    door_1_locked = "πͺ Door 1"
    door_2_locked = "πͺ Door 2"
    door_3_locked = "πͺ Door 3"
    door_1_unlocked = f"{symbols[0]} Door 1"
    door_2_unlocked = f"{symbols[1]} Door 2"
    door_3_unlocked = f"{symbols[2]} Door 3"
    print(f"{door_1_locked} - {door_2_locked} - {door_3_locked}")


    try:
        input_one = int(input("π Your First Answer : "))
        if (input_one != 1) and (input_one != 2) and (input_one != 3):
            raise ValueError
    except ValueError:
        clear()
        try:
            result_for_change = (changed.count("WIN") / (changed.count("WIN") + changed.count("LOSE"))) * 100
        except ZeroDivisionError:
            result_for_change = "No Info"
        try:
            result_for_notchange = (notchanged.count("WIN") / (notchanged.count("WIN") + notchanged.count("LOSE"))) * 100
        except ZeroDivisionError:
            result_for_notchange = "No Info"
        print("\n")
        print("".center(50,"|"))
        print(f" Win chance when changed : %{result_for_change} ".center(50," "))
        print(f" Win chance when not changed : %{result_for_notchange} ".center(50," "))
        print("".center(50,"|"))
        break
    

    while True:
        computer_selected = choice(doors)
        computer_selected_index = doors.index(computer_selected)
        if (input_one-1) != computer_selected_index and symbols[computer_selected_index] != "π":
            break
    

    if computer_selected_index == 0:
        print(f"\n{door_1_unlocked} - {door_2_locked} - {door_3_locked}")
    elif computer_selected_index == 1:
        print(f"\n{door_1_locked} - {door_2_unlocked} - {door_3_locked}")
    elif computer_selected_index == 2:
        print(f"\n{door_1_locked} - {door_2_locked} - {door_3_unlocked}")


    while True:
        try:
            input_two = int(input("π Your Second Answer : "))
            if (input_two != 1) and (input_two != 2) and (input_two != 3):
                raise ValueError
            else:
                break
        except ValueError:
            pass
    if symbols[input_two-1] == "π":
        result = "WIN βοΈ"
    else:
        result = "LOSE β"


    print("")
    print(f" Result : {result} ".center(26,"-"))
    print(f"{door_1_unlocked} - {door_2_unlocked} - {door_3_unlocked}")
    sleep(game_speed)


    if input_one == input_two and symbols[input_two-1] == "π":
        notchanged.append("WIN")
    elif input_one == input_two and symbols[input_two-1] == "π":
        notchanged.append("LOSE")
    elif input_one != input_two and symbols[input_two-1] == "π":
        changed.append("WIN")
    elif input_one != input_two and symbols[input_two-1] == "π":
        changed.append("LOSE")
