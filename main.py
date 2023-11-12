import json
# додав інструкцію, щоб учасники зрозуміли правила
instructions = """
This will be our tic tac toe board

 (1,1) | (2,1) | (3,1) 
-------|-------|------
 (1,2) | (2,2) | (3,2) 
-------|-------|------
 (1,3) | (2,3) | (3,3) 

*instructions:
0. yoy have a devision, choose new game or start from last check point
1. Insert the couple of numbers (1-3) to put your sign,
2. You must fill all  spots to get result,
3. Player 1 will go first.
4. if you wanna save your game and continue, any player may write "7 7" and confirm saving
"""


def print_board(sign_dict):
    for i in range(3):
        row = []
        for j in range(3):
            row.append(sign_dict[i][j])
        print(" | ".join(row))
        if i < 2:
            print("---------")


index_list = []


def take_input(player_name,sign_dict):
    while True:
        x, y = map(int, input(f'{player_name}: ').split())
        x -= 1
        y -= 1
        if 0 <= x <= 2 and 0 <= y <= 2:
            if (x, y) in index_list:
                print('This spot is blocked.')
                continue
            index_list.append((x, y))
            return x, y
        elif x == 6 and y == 6:
            check_point = input("Do you realy want to save game?:")
            if check_point == "yes":
                saving(sign_dict)
                exit()
            else:
                continue
        else:
            print("Fail!, try again")
            continue
# поставив continue щоб якщо гравець поставив якусь фігню, то він переграв

#два методи, один записує в файл поточну таблицю, другий читає збережену таблицю, коли потрібно
def saving(sign_dict):
    with open('check_point.json', 'w') as file:
        json.dump(sign_dict, file)
def reader():
    with open('check_point.json', 'r') as file:
        sign_dict = json.load(file)
    return sign_dict

def betterResult_calculation(sign_dict, player_one, player_two):
    for i in range(3):
        if sign_dict[i][0] == sign_dict[i][1] == sign_dict[i][2] == "X":
            print(f'Congratulations {player_one}. You WON.!!')
            # quit('Thank you both for joining')
            return True
        elif sign_dict[i][0] == sign_dict[i][1] == sign_dict[i][2] == "O":
            print(f'Congratulations {player_two}. You WON.!!')
            # quit('Thank you both for joining')
            return True
    for j in range(3):
        if sign_dict[0][j] == sign_dict[1][j] == sign_dict[2][j] == "X":
            print(f'Congratulations {player_one}. You WON.!!')
            # quit('Thank you both for joining')
            return True
        elif sign_dict[0][j] == sign_dict[1][j] == sign_dict[2][j] == "O":
            print(f'Congratulations {player_two}. You WON.!!')
            # quit('Thank you both for joining')
            return True

    main_diagonal = [sign_dict[i][i] for i in range(len(sign_dict))]
    if all(element == "X" for element in main_diagonal):
        print(f'Congratulations {player_one}. You WON.!!')
        # quit('Thank you both for joining')
        return True
    elif all(element == "O" for element in main_diagonal):
        print(f'Congratulations {player_two}. You WON.!!')
        # quit('Thank you both for joining')
        return True
    side_diagonal = [sign_dict[i][len(sign_dict) - 1 - i] for i in range(len(sign_dict))]
    if all(element == "X" for element in side_diagonal):
        print(f'Congratulations {player_one}. You WON.!!')
        # quit('Thank you both for joining')
        return True
    elif all(element == "O" for element in side_diagonal):
        print(f'Congratulations {player_two}. You WON.!!')
        # quit('Thank you both for joining')
        return True
    return False


def main():
    print("Welcome to  tic tac toe game.!!")
    player_one = input("Enter player 1 name: ")
    player_two = input("Enter player 2 name: ")
    print(f"Thank you for joining Mr./Mrs. {player_one} and Mr./Mrs. {player_two}")
    print(instructions)
    print(f"Mr. {player_one}'s sign is - X")
    print(f"Mr. {player_two}'s sign is - O")
    reading=input("Do you want to start from last check point:")
    if reading=="yes":
        sign_dict=reader()
    else:
        sign_dict = [[' ' for _ in range(3)] for _ in range(3)]

    print_board(sign_dict)
    for i in range(0, 9):
        if i % 2 == 0:
            index = take_input(player_one,sign_dict)
            sign_dict[index[0]][index[1]] = 'X'
        else:
            index = take_input(player_two,sign_dict)
            sign_dict[index[0]][index[1]] = 'O'
        print_board(sign_dict)

        if betterResult_calculation(sign_dict, player_one, player_two):
            return


if __name__ == "__main__":
    main()
