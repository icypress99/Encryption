MAX = 1000000007

def hash(message):
    res = 1
    for c in message:
        res = res * ord(c) % MAX
    return res

def play_game(random_string, guess, br):
    if len(random_string) <= 8:
        print("The random string's length is too short Abbas!")
        return
    hashed_value = hash(br + random_string)

    if guess == "H":
        if hashed_value % 2 == 0:
            print("You won Abbas! 100$ is yours")
        else:
            print("I won Abbas! You ain't get the 100$.")
    elif guess == "T":
        if hashed_value % 2 != 0:
            print("You won Abbas! 100$ is yours")
        else:
            print("I won Abbas! You ain't get the 100$.")
    else:
        print("Invalid guess!")

random_string = input()
guess = input()
br = input()

play_game(random_string, guess, br)