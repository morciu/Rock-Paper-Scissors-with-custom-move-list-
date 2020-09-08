from random import choice


def player_move(moves):
    move = input().lower()
    return move


def computer_move(moves):
    c_move = choice(moves)
    return c_move


def check_game(p_move, c_move):
    status = ""
    if p_move == c_move:
        message = f"There is a draw ({p_move})"
        status = 'draw'
    elif (p_move == 'rock' and c_move == 'scissors') or \
            (p_move == 'paper' and c_move == 'rock') or \
            (p_move == 'scissors' and c_move == 'paper'):
        message = f"Well done. The computer chose {c_move} ad failed"
        status = 'win'
    elif (p_move == 'rock' and c_move == 'paper') or \
            (p_move == 'paper' and c_move == 'scissors') or \
            (p_move == 'scissors' and c_move == 'rock'):
        message = f"Sorry, but the computer chose {c_move}"
        status = 'lose'
    return message, status

def get_name(file):
    new = False
    name = input('Enter your name: ')
    print(f"Hello, {name}")
    with open(file, 'r') as f:
        if name not in f.read().split():
            new = True
    if new:
        with open(file, 'a') as f:
            f.write(f"{name} 0\n")
    return name

def check_score(file, name):
    current_score = 0
    with open(file, 'r') as f:
        for line in f.readlines():
            if line.split()[0] == name:
                current_score = int(line.split()[1])
                print(line.split()[1])
    return current_score

def update_score(status, file, name):
    scores = {}
    score_sheet = open(file, 'r')
    for line in score_sheet.readlines():
        scores[line.split()[0]] = line.split()[1]
    score_sheet.close()
    if status == 'draw':
        new_score = 50 + int(scores[name])
    elif status == 'win':
        new_score = 100 + int(scores[name])
    else:
        new_score = 0 + int(scores[name])
    scores[name] = str(new_score)
    with open(file, 'w') as f:
        for key, value in scores.items():
            f.write(f"{key} {value}\n")
    return scores

def check_custom_moves(moves, p_move, c_move):
    inferior_moves = []
    superior_moves = []
    x = 0
    if p_move in moves:
        for i in range(1, int((len(moves) - 1) / 2) + 1):
            try:
                superior_moves.append(moves[moves.index(p_move) + i])
            except IndexError:
                superior_moves.append(moves[x])
                x += 1
    for i in moves:
        if i not in superior_moves and i != p_move:
            inferior_moves.append(i)
    if p_move == c_move:
        message = f"There is a draw ({p_move})"
        status = 'draw'
    elif c_move in inferior_moves:
        message = f"Well done. The computer chose {c_move} ad failed"
        status = 'win'
    elif c_move in superior_moves:
        message = f"Sorry, but the computer chose {c_move}"
        status = 'lose'
    return message, status

def run_game():
    ratings = 'rating.txt'
    standard = False
    custom = False
    available_moves = ['rock', 'paper', 'scissors']
    name = get_name(ratings)
    game_mode = input()
    if game_mode == '':
        standard = True
        print("Ok, let's start")
    else:
        custom = True
        print("Okay, let's start")
    while standard:
        move = player_move(available_moves)
        if move == '!exit':
            print('Bye!')
            break
        elif move == '!rating':
            score = check_score(ratings, name)
            print(f"Your rating: {score}")
            continue
        elif move != '!exit' and move not in available_moves:
            print('Invalid input')
            continue
        ai_move = computer_move(available_moves)
        message, status = check_game(move, ai_move)
        update_score(status, ratings, name)
        print(message)
    while custom:
        custom_moves = game_mode.split(',')
        move = player_move(custom_moves)
        if move == '!exit':
            print('Bye!')
            break
        elif move == '!rating':
            score = check_score(ratings, name)
            print(f"Your rating: {score}")
            continue
        elif move != '!exit' and move not in custom_moves:
            print('Invalid input')
            continue
        ai_move = computer_move(custom_moves)
        message, status = check_custom_moves(custom_moves, move, ai_move)
        update_score(status, ratings, name)
        print(message)


run_game()