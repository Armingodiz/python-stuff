import random , time

fruits = ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple','cantaloupe', 'grapefruit','jackfruit','papaya'] 
superHeroes = ['hawkeye', 'robin', 'Galactus', 'thor', 'mystique', 'superman', 'deadpool', 'vision', 'sandman', 'aquaman']
countries = [ 'iran','america','spain','iraq','england','poland']
names = ['armin','hadi','sina','saba','farzad','amirhossein','amir']

def start(name):
    catg = input("categories : \n 1) fruits\n 2) superHeroes\n 3) countries \n 4) names \n")
    secretWord = ""
    if catg =="1":
        secretWord = random.choice(fruits)
    elif catg =="2":
        secretWord = random.choice(superHeroes)
    elif catg =="3":
        secretWord = random.choice(countries)
    elif catg=="4":
        secretWord = random.choice(names)
    else:
        print("INVALID input !")
        startGame(name)
    startGame(secretWord)
    inp = input("1) PLAY AGAIN\n2) EXIT ! \n")
    if inp=="1":
        start(name)

def startGame(secretWord):
    points = 0
    shots = len(secretWord) + 4
    gusses =list()
    for n in secretWord :
        gusses.append('__ ')
    while shots != 0 :
        print("the word is : ")
        print(gusses)
        guess = input("ENTER YOUR GUESS :\n")
        shots -= 1
        for index in range(len(secretWord)) :
            if guess == secretWord[index] and gusses[index] == '__ ':
                print("nice guess !")
                points += 1
                gusses[index] = guess
                break
        else :
            print("NO ) : ")
        if shots + points < len(secretWord) or len(secretWord)==points:
            break
    print("THE WORD IS : ",end=" ")
    print(secretWord)
    print("YOUR GUESS : ",end=" ")
    print(str(gusses))
    if len(secretWord) == points :
        print("VICTORY !")
    else :
        print("DEFEATE !")



name = input("Enter your name \n")
print("Hello ", name.capitalize(), "let's play Hangman!")
time.sleep(1)
print("The objective of the game is to guess the secret word chosen by the computer.")
time.sleep(1)
print("You can guess only one letter at a time. Don't forget to press 'enter key' after each guess.")
time.sleep(1)
start(name)



    





    