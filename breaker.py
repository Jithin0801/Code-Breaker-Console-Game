# A simple command line game


#The game goes like this:
# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!


import random



MATCH = "One of the digits is a match!"
CLOSE = "You are close!"
NOT_CLOSE = "Not even close!"
CORRECT = "Oh! you got me correctly!"
guess_flag = 0
def get_guess():
    global guess_flag
    if guess_flag == 0:
        return list(input("What is you guess? "))
    else:
        return list(input("Guess again! "))


def generate_code():
    l = [str(i) for i in range(10)]
    random.shuffle(l)
    return l[:3]

def generate_result(clue):
    return MATCH if MATCH in clue else CLOSE if CLOSE in clue else NOT_CLOSE


def find_guess(code, user_code):
    global guess_flag
    clue = []
    if code == user_code:
        return CORRECT
    else:
        for index, num in enumerate(user_code):
            guess_flag = 1
            if num == code[index]:
                clue.append(MATCH)
            elif num in code:
                clue.append(CLOSE)
            else:
                clue.append(NOT_CLOSE)

    result = generate_result(clue)

    return result


def game():
    guess = []
    code = generate_code()
    f = open("code.txt", "w")
    st = "".join(code)
    f.write(st)
    f.close()
    while guess != CORRECT:
        user_code = get_guess()
        guess = find_guess(code, user_code)
        print(guess)
        

#Driver code
flag = 0
def main(): 
    ans = "Y"
    global flag
    while ans == "Y" or ans == "y":
        if flag == 1:
            print("Continue the game? (Y-Yes/N-No)")
        else:
            print("Hello, Code Breaker!")
            print("Start the game? (Y-Yes/N-No)")
        ans = input()
        if ans == "Y" or ans == "y":
            flag = 1
            game()
        else:
            break

main()
