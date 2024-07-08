import random

from word import words

word = list(",".split())
word = random.choice(words)

jumble = "".join(random.sample(word,len(word)))
chances = 3

print("~"*30)
print("~~~ Avengers Jumble Bumble ~~~")
print("~"*30)

while chances != 0:
    print(f"the word is {jumble}")

    guess = input("enter your guesses word: ")

    if guess == word:
        print("You guess the correct. Congratulations!")
        print(f"The word is {word}")
        break
    else:
        chances -= 1
  
        print("Sorry, you guess the wrong word")
        print(f"Remaining the chances are {chances}")

        print()
else:
    print("You lost the game")
    print(f"The correct word is {word}")
print("Thank for playing")