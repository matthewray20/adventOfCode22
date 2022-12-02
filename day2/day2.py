#!/usr/bin/env python3

FILENAME = 'stragety_guide.txt'


def part1():
    # oppenents_move, my_move
    rpc_outcomes = {
        ('rock', 'rock'):3,
        ('paper', 'paper'):3,
        ('scissors', 'scissors'):3,
        ('rock', 'paper'):6,
        ('rock', 'scissors'):0,
        ('paper', 'rock'):0,
        ('paper', 'scissors'):6,
        ('scissors', 'rock'):6,
        ('scissors', 'paper'):0
    }
    total_score = 0
    # for readability
    mappings = {'A':'rock', 'B':'paper', 'C':'scissors', 'X':'rock', 'Y':'paper', 'Z':'scissors'}
    shape_points = {'rock':1, 'paper':2, 'scissors':3 }
    with open(FILENAME, 'r') as f:
        for line in f:
            line = line.strip('\n')
            for key in mappings:
                line = line.replace(key, mappings[key])
            opponent_move, my_move = line.split()
            total_score += shape_points[my_move] + rpc_outcomes[opponent_move, my_move]
    print(f'total score: {total_score}')


def part2():
    total_score = 0
    move_to_make = {
        ('rock', 'lose'):'scissors',
        ('rock', 'draw'):'rock',
        ('rock', 'win'):'paper',
        ('paper', 'lose'):'rock',
        ('paper', 'draw'):'paper',
        ('paper', 'win'):'scissors',
        ('scissors', 'lose'):'paper',
        ('scissors', 'draw'):'scissors',
        ('scissors', 'win'):'rock'
    }
    # for readability
    mappings = {'A':'rock', 'B':'paper', 'C':'scissors', 'X':'lose', 'Y':'draw', 'Z':'win'}
    outcome_points = {'lose':0, 'draw':3, 'win':6}
    shape_points = {'rock':1, 'paper':2, 'scissors':3 }
    with open(FILENAME, 'r') as f:
        for line in f:
            line = line.strip('\n')
            for key in mappings:
                line = line.replace(key, mappings[key])
            opponent_move, match_outcome = line.split()
            my_move = move_to_make[opponent_move, match_outcome]
            total_score +=  shape_points[my_move] + outcome_points[match_outcome]
    print(f'total score: {total_score}')




if __name__ == '__main__':
    part1()
    part2()