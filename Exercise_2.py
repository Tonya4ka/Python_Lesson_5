# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

import random           

message = "You can take from 1 to 28 of the candies"

def play_game(n, m, players, message):
    count = 0
    while n > 0:
        print(f'{players[count%2]}, {message}')
        move = int(input())
        if move > n or move > m:
            print(f'Too much, you can take not more than {m} candy(ies), we have only {n} candy(ies)')
            continue
        n = n - move
        if n > 0: print(f'{n} candy(ies) left')
        else: print('No more candies left')
        count +=1
    return players[not count%2]

player1 = "1-st player"
player2 = "2-nd player"
players = [player1, player2]

n = 2021
m = 28

winer = play_game(n, m, players, message)
print(f'{winer} is winer')