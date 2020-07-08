"""
import game
import random

number = random.randint(1,10)
while True:
    guess_number = int(input("请输入你猜测的10以内数字:"))
    if game.IsCorrect(guess_number, number) == True:
        print("恭喜你猜对了！")
        break
    elif game.IsCorrect(guess_number, number) == "lower":
        print("你猜的小了")
    elif game.IsCorrect(guess_number, number) == "higher":
        print("你猜的大了")
"""





