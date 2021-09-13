import math
import os
import random
import re
import sys


def search(ranked, rank):
    for i in range(len(ranked)):
        if i == 0:
            if rank <= ranked[i] and rank >= ranked[i+1]:

                return (i+1)+1
            elif rank > ranked[i]:

                return i+1
        elif i == (len(ranked)-1):
            if rank >= ranked[i] and rank <= ranked[i+1]:

                return (i+1)
            elif rank < ranked[i]:

                return (i+1)+1
        else:
            if rank <= ranked[(len(ranked)-1)-i] and rank >= ranked[(len(ranked)-1)-(i-1)]:

                return (len(ranked)-i)+1


def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked))
    ranked.reverse()
    rank_list = []
    for rank in player:
        rank_list.append(search(ranked, rank))
    print(rank_list)
    return rank_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
