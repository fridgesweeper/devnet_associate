"""
校验猜测数字是否正确函数
"""

#guess_number是用户猜测数字
#number是被猜测数字

def IsCorrect(guess_number, number):
    if guess_number == number:
        return True
    elif guess_number < number:
        return "lower"
    elif guess_number > number:
        return "higher"
