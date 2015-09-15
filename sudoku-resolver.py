import operator
import copy
'''
a sudoku resolver
'''
def check(u):
    t = range(1,10)
    u.sort()
    if t == u:
        return True
    else:
        return False

def get_row(game,r):
    row = game[r*9:(r+1)*9]
    return row

def get_column(game,c):
    column = [game[i*9+c] for i in range(0, 9)]
    return column

def get_block_by_id(game, x, y):
    block = game[x*3*9+y*3:x*3*9+y*3+3] \
            + game[(x*3+1)*9+y*3:(x*3+1)*9+y*3+3] \
            + game[(x*3+2)*9+y*3:(x*3+2)*9+y*3+3]
    #print block
    return block

def get_block(game, r, c):
    return get_block_by_id(game, r/3, c/3)

def check_row(game, r):
    row = get_row(game, r)
    return check(row) 

def check_column(game, c):
    column = get_column(game, )
    return check(column)

def check_block_by_id(game, x, y):
    block = get_block_by_id(game, x, y)
    return check(block)

def find_miss(l):
    t = range(1,10)
    for i in l:
        if i != 0:
            t.remove(i)
    return t 

def find_empty(game):
    l = []
    for r in range(0, 9):
        for c in range(0, 9):
            if game[r*9+c] == 0:
                l.append((r, c))
    return l

def list_and(l1, l2, l3):
    lt = []
    result = []
    for i in l1:
        if l2.count(i) == 1:
            lt.append(i)
    for i in lt:
        if l3.count(i) == 1:
            result.append(i)
    return result

result = []

def print_game(game):
    print "==========================="
    for i in range(0, 9):
        print game[i*9:(i+1)*9]
    print "==========================="

step = 0
def find_possible(game):
    global step
    step += 1
    possible = {}
    #print_game(game)
    empty = find_empty(game)
    game_copy = copy.deepcopy(game)
    if len(empty) == 0:
        #print "solved"
        return game 
    changed = False
    for (r, c) in empty:
        r_candi = find_miss(get_row(game, r))
        c_candi = find_miss(get_column(game, c))
        b_candi = find_miss(get_block(game, r, c))
        candi = list_and(r_candi, c_candi, b_candi)
        if len(candi) == 0:
            #print "False impossbile"
            return False
        elif len(candi) == 1:
            #print 'Decided', (r, c), candi[0]
            game_copy[r*9+c] = candi[0]
            return find_possible(game_copy)
        else:
            possible[(r, c)] = candi

    possible_sorted = sorted(possible.items(), key=lambda x: len(x[1]))
    
    ((r, c), pos) = possible_sorted[0]
    #print (r, c), pos
    for v in pos: 
        #print 'possible', (r, c), v
        game_copy[r*9+c] = v
        #print "guess"
        #print_game(game_copy)
        result = find_possible(game_copy)
        if result == False:
            pass
        else:
            return result
    return False

def verify(game):
    for r in range(0,9):
        if check(get_row(game, r)):
            pass
        else:
            print 'r', r
            return False
    for c in range(0,9):
        if check(get_column(game, c)):
            pass
        else:
            print 'c', c
            return False
    for x in range(0,3):
        for y in range(0,3):
            if check(get_block(game, x, y)):
                pass
            else:
                print 'b', (x,y)
                return False
    return True

def resolve(game):
    global step
    step = 0
    print 'problem'
    print_game(game)
    result = find_possible(game)
    if result == False:
        print "game error"
    else:
        print 'results'
        print_game(result)
        if verify(result) == True:
            print 'result ok'
            print 'total steps', step
            step = 0
        else:
            print 'result error'

game1 = [
        0, 3, 0, 0, 0, 1, 2, 0, 5,
        0, 0, 4, 5, 0, 0, 0, 7, 0,
        2, 0, 0, 8, 0, 0, 0, 0, 9,
        9, 8, 2, 0, 0, 0, 0, 3, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 4, 0, 0, 0, 0, 7, 9, 2,
        4, 0, 0, 0, 0, 7, 0, 0, 8,
        0, 2, 0, 0, 0, 4, 1, 0, 0,
        7, 0, 3, 6, 0, 0, 0, 5, 0,
        ]

game2 = [
        0, 0, 9, 0, 0, 1, 0, 0, 8,
        3, 0, 0, 7, 6, 9, 0, 0, 0,
        1, 0, 0, 0, 0, 8, 0, 9, 0,
        0, 0, 0, 0, 7, 0, 0, 2, 3,
        5, 3, 7, 0, 0, 0, 8, 6, 1,
        2, 8, 0, 0, 1, 0, 0, 0, 0,
        0, 2, 0, 6, 0, 0, 0, 0, 5,
        0, 0, 0, 5, 9, 7, 0, 0, 2,
        7, 0, 0, 1, 0, 0, 3, 0, 0,
        ]

resolve(game1)
resolve(game2)
