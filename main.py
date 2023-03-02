import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

# return true if player wins
def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or \
            (player == 'p' and opponent == 'r'):
        return True
    return False

def main():
    play_again = True
    while play_again:
        result, user, computer = play()
        if result == 0:
            print(f'Both players chose {user}. It\'s a tie!')
        elif result == 1:
            print(f'You chose {user} and the computer chose {computer}. You won!')
        else:
            print(f'You chose {user} and the computer chose {computer}. You lost!')
        answer = input("Do you want to play again? (Y/N)").lower()
        if answer != 'y':
            play_again = False

if __name__ == '__main__':
    main()
