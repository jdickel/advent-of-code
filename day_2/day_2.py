
# Rock          A   X   1 point
# Paper         B   Y   2 points
# Scissors      C   Z   3 points

# loss                  0 points
# draw                  3 points
# win                   6 points

ROCK_POINTS = 1
PAPER_POINTS = 2
SCISSORS_POINTS = 3

LOSS_POINTS = 0
DRAW_POINTS = 3
WIN_POINTS = 6

def get_player_picks(line: str):
    picks = line.strip().split(' ')
    return picks[0],  picks[1]


def get_pick_points(my_pick):
    if my_pick == 'X':
        return ROCK_POINTS
    elif my_pick == 'Y':
        return PAPER_POINTS
    else:
        return SCISSORS_POINTS

def get_round_outcome_points(opponent_pick, my_pick):
    if (opponent_pick == 'A' and my_pick == 'X') or (opponent_pick == 'B' and my_pick == 'Y') or (opponent_pick == 'C' and my_pick == 'Z'):
        return DRAW_POINTS
    elif (opponent_pick == 'A' and my_pick == 'Y') or (opponent_pick == 'B' and my_pick == 'Z') or (opponent_pick == 'C' and my_pick == 'X'):
        return WIN_POINTS
    else:
        return LOSS_POINTS


def get_total_round_points(opponent_pick, my_pick):
    round_points = 0
    round_points += get_pick_points(my_pick)
    round_points += get_round_outcome_points(opponent_pick, my_pick)
    print(round_points)

    return round_points


total_points = 0

with open('input.txt', encoding='utf-8') as f:
    for line in f:
        opponent_pick, my_pick = get_player_picks(line)
        total_points += get_total_round_points(opponent_pick, my_pick)


print("Part 1: ")
print(total_points)

