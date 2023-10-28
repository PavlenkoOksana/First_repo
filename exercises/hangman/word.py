import random
from const import FILENAME_MAPPING


class Word:
  def __init__(self, word_len):
    word_file = FILENAME_MAPPING.get(word_len)
    with open(word_file, mode='r') as file_stream:
      word = random.choice(file_stream.readlines())
      print(word)
    self.__word=list(word[0:-1])
    self.__guessed_word = ["_"]*word_len
    self.__missed_letters = []
    self.word_len = word_len
    
  def check_letter(self, letter):
    contains_letter = False
    for i in range(len(self.__word)):
      if self.__word[i] == letter:
        contains_letter = True
        self.__guessed_word[i] = letter
            
    if not contains_letter:
      self.__missed_letters.append(letter)
    return contains_letter
  
  def is_word_guessed(self):
    print("hidden word:  "+" ".join(self.__guessed_word)+f" ({self.word_len} letters) ")
    print("your unguessed letters:  ", ", ".join(self.__missed_letters))
    return self.__guessed_word == self.__word
  
  def get_word(self):
    return self.__word
  
  def get_missed_letters(self):
    return self.__missed_letters


