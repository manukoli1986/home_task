import random  # import random module


def randomNum():  # Creating randomNum method 
    num = 0
    num = list(range(1,11))
    random.shuffle(num)
    print(num)


randomNum()   # Printnumbers from 1 to 10