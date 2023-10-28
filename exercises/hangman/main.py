import random
from man import Man
from word import Word
from const import GALLOWS

def main():
  letters = random.randint(5,7)
  word = Word(letters)
  man = Man()
  print("\n"*50,"\033[1m\033[34m{}\033[0m".format("Welcome to the game!"))
  print("to exit the game enter 'end'")
  
  print(GALLOWS[0])
  while not man.is_game_over() and not word.is_word_guessed():
    guess = input()
    if guess == "end":
      print("\n"*50,"\033[1m\033[34m{}\033[0m".format("٩(｡•́‿•̀｡)۶"))
      print("\n"*3,"\033[1m\033[34m{}\033[0m".format("See you later!"))      
      break
    elif word.check_letter(guess):
      print("\n"*50,"\033[32m{}\033[0m".format("you guessed the letter!"))
    else:
      man.add_body_part()
      print("\033[31m{}\033[0m".format("you did not guessed the letter."))
      
  else:
    if word.is_word_guessed():
        print("\n"*50)
        print(("\033[32m{}\033[0m".format("(◕‿◕ )" + "\n"*3)))
        print(("\033[32m{}\033[0m".format("You won!!!!" + "\n"))*3)
        print("\n"*3)
    else:
        print("\n"*50)
        print("\033[31m{}\033[0m".format("(︶︹︺) "+ "\n"*3))
        print("\033[31m{}\033[0m".format("You lose."))
        print("\n"*3)

if __name__ == "__main__":
  main()