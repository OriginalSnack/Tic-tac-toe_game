def print_board(sign_dict):
    for i in range(3):
        row = []
        for j in range(3):
            row.append(sign_dict[i][j])
        print(" | ".join(row))
        if i < 2:
            print("---------")


index_list = []


def take_input(player_name):
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


#       _(0,0)_|_(1,0)_|_(2,0)_
#       _(0,1)_|_(1,1)_|_(1,2)_
#        (0,2) | (1,2) | (2,2)

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
    print("Welcome to sunny's tic tac toe game.!!")
    player_one = input("Enter player 1 name: ")
    player_two = input("Enter player 2 name: ")
    print(f"Thank you for joining Mr./Mrs. {player_one} and Mr./Mrs. {player_two}")
    print(f"Mr. {player_one}'s sign is - X")
    print(f"Mr. {player_two}'s sign is - O")
    input("Enter any key to start the game: ")

    sign_dict = [[' ' for _ in range(3)] for _ in range(3)]

    print_board(sign_dict)
    for i in range(0, 9):
        if i % 2 == 0:
            index = take_input(player_one)
            sign_dict[index[0]][index[1]] = 'X'
        else:
            index = take_input(player_two)
            sign_dict[index[0]][index[1]] = 'O'

        print_board(sign_dict)

        if betterResult_calculation(sign_dict, player_one, player_two):
            return


if __name__ == "__main__":
    main()
