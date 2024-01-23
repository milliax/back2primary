""" This is the advanced python project """

import os

# 終極數字

final_answer = 10
guessed_time = 0
passed = False

print("猜數字遊戲!!")
print("每個人可以有10次機會猜出一開始的數字是多少")
print("範圍介於 1 到 100 之間")

final_answer = int(input("請輸入數字: "))
os.system('tput reset')

for i in range(10):
    # 輸入數字
    print("\n第{}次猜測".format(guessed_time+1))
    number = int(input("你要猜的數字: "))
    guessed_time += 1

    if (number == final_answer):
        print("恭喜你找到答案了")
        print("答案是: ", final_answer)
        passed = True
        break
    elif (number > final_answer):
        print("再猜小一點")
    else:
        print("再猜大一點")


if not passed:
    print("好可惜你差一點就猜出答案了")
    print("答案是{}".format(final_answer))
