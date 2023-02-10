# 导入相关模块
import random
import time
import os
os.system('')

# 初始化棋盘，设定棋盘的行数和列数
MX = 8
MY = 8

# 初始化雷的数量
MINE_NUM = 10

# 创建二维数组，用来存储游戏棋盘
board = [[0 for i in range(MY)] for j in range(MX)]

# 初始化游戏棋盘，将雷放置到棋盘中
mine_pos = random.sample(range(MX*MY), MINE_NUM)
for pos in mine_pos:
    OYpos = pos // MY
    OXpos = pos % MY
    board[OYpos][OXpos] = -1

# 根据雷的位置，计算棋盘中每个格子的数字
for OYpos in range(MX):
    for OXpos in range(MY):
        if board[OYpos][OXpos] == -1:
            continue
        else:
            mine_count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= OYpos + i < MX and 0 <= OXpos + j < MY:
                        if board[OYpos+i][OXpos+j] == -1:
                            mine_count += 1
            board[OYpos][OXpos] = mine_count
# 一些留言
print("\033[1;32m我发誓这绝对是全网最蠢的游戏，玩这个游戏你甚至需要一张纸和一支笔来记下雷的位置。\n棋盘是8x8格式，有10个雷，玩法与传统的一样,数字从左到右从上到下0~8顺序排列\033[0m")
# 打印游戏棋盘
print("\033[1;31m开始计时！祝你好运！\033[0m")
for OYpos in range(MX):
    for OXpos in range(MY):
        print('* ', end='')
    print()

# 判断是否全部翻开
def is_all_open():
    for OYpos in range(MX):
        for OXpos in range(MY):
            if board[OYpos][OXpos] != -1 and board[OYpos][OXpos] != '*':
                return False
    return True



# 开始游戏

start_time = time.time()
while True:
    # 用户输入要翻开的格子
    OYpos = int(input('你要翻开哪一行的格子：'))
    OXpos = int(input('你要翻开哪一列的格子：'))
    # 判断翻开的格子是否是雷
    if board[OYpos][OXpos] == -1:
        print("\033[1;31m你踩到雷了，游戏结束！\033[0m")
        break
    else:
        print('这个格子的数字是：', board[OYpos][OXpos])
        # 判断是否全部翻开
        if is_all_open():
            end_time = time.time()
            print("\033[1;32m恭喜你，游戏成功！用时：\033[0m", end_time - start_time)
            break


