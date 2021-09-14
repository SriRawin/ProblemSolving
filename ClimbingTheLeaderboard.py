import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked))
    ranked.reverse()
    rank_list = []
    n=len(ranked)
    for rank in player:
        while n>0 and rank>=ranked[n-1]:
            n-=1
        rank_list.append(n+1)
   
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
