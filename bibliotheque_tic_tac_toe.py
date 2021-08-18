from sys import stdin,stdout
from copy import deepcopy

global deltas,positions, DIM, JOUEUR, IA,INF, DEPTH
DIM = 3
JOUEUR, IA = "X", "O"
INF = float('inf')
DEPTH = 10
deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
positions = [(x,y) for y in range(DIM) for x in range(DIM)]

def valide_pos(x,y):
    return (0<= x < DIM and 0<= y < DIM)
    
def test_win(joueur, carte):
    for x, y in positions:
        if carte[x][y] == joueur:
            for d_x,d_y in deltas:
                x1, y1, x2,y2 = x+d_x, y+d_y, x+2*d_x, y + 2*d_y
                if valide_pos(x1,y1) and valide_pos(x2,y2) and carte[x1][y1] == joueur and carte[x2][y2] == joueur:
                    return True
    return False
def test_fin(carte):
    FIN = True
    for x,y in positions:
        if carte[x][y].isdigit():
            FIN = False
    return FIN
  
def game_over(carte):
    return (test_win(IA,carte) or test_win(JOUEUR,carte) or test_fin(carte))


def best_mouv(carte):
    best_score = -INF
    for x, y in positions:
        if carte[x][y].isdigit():
            carte[x][y] = IA
            score = minimax(carte,DEPTH, -INF, INF,False)
            carte[x][y] = "0"
            if score > best_score:
                best_score = score
                best = (x,y)
    print(best, best_score)
    return best
    
def minimax(carte,depth, alpha, beta,ia):
    # Match gagnant
    if test_win(IA,carte): return depth
    if test_win(JOUEUR,carte): return -depth
    # Match nul
    if depth == 0 or test_fin(carte):
        return 0
    
    if ia:
        score = -INF
        for x,y in positions:
            if carte[x][y].isdigit():
                carte[x][y] = IA
                score = max(score,minimax(carte, depth - 1, alpha, beta, False))
                carte[x][y]= "0"
                
                if score >= beta:
                   return score
                alpha = max(alpha, score)
                
        return score
    else:
        score = INF
        for x,y in positions:
            if carte[x][y].isdigit():
                carte[x][y] = JOUEUR
                score = min(score,minimax(carte, depth - 1, alpha, beta, True))
                carte[x][y]= "0"
                if alpha >= score:
                    return score
                beta = min(score,beta)
                
        return score

""""
def best_mouv2(carte):
    best_score = -INF
    best = (DIM,DIM)
    for x, y in positions:
        if carte[x][y].isdigit():
            carte[x][y] = IA
            score = minimax2(carte,9, -INF,False)
            carte[x][y] = str(x*DIM+y+1)
            if score > best_score:
                best_score = score
                best = (x,y)
    print(best, best_score)
    return best
def minimax2(carte,depth,score,ia):
    if depth == 0 or game_over(carte):
        return depth
    if ia:
        maxEval = -INF
        for x,y in positions:
            if carte[x][y].isdigit():
                carte[x][y] = IA
                score = minimax2(carte, depth - 1,score, False)
                carte[x][y]= str(x*DIM+y+1)
                maxEval = max(maxEval, score)
        return max(score, maxEval)
    else:
        for x,y in positions:
            if carte[x][y].isdigit():
                carte[x][y] = JOUEUR
                if test_win(JOUEUR,carte):
                    carte[x][y]= str(x*DIM+y+1)
                    return -INF
                carte[x][y]= str(x*DIM+y+1)
        return minimax2(carte, depth - 1,score, True)
"""
