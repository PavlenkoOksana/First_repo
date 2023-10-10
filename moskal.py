import calendar
from faker import Faker
from constans import MENU
from exeption import NotInRange
from pathlib import Path

FILENAME = Path(__file__).parent / "losses.txt"
print(FILENAME)

def add_new_record (name, amount):
  with open (FILENAME, "a") as f:
    fake= Faker()
    current_date = fake.date_between("-1y").strftime("%m/%d/%Y")
    print(current_date)
    record = f"{current_date: >15}{name: ^40}{amount: ^10}\n"
    f.write(record)
    
def show_statistics():
  with open (FILENAME, "r") as f:
    lines = f.readlines()
    for line in lines:
      print(line, end="")
    

while True:
  print(MENU)
  try:
    choice = int(input("Make your chois  "))
    if choice < 1 and choice >5:
      raise NotInRange
  except ValueError:
    print ("Please make your choice")
    continue
  except NotInRange:
    print("Choise potion from 1-5")
    continue
  if choice == 1:
    print("please enter data in following format: <name>:<amount>")
    try:
      s = input (">>> ")
      name, count = s.split(":")
    except: 
      print("try again")
      continue
    add_new_record(name, count)
  elif choice == 2:
    print("Please see data below: ")
    show_statistics()
  elif choice == 3:
    print("Enter year: ")
    try:
      year = int(input(">>>>"))
      text = calendar.calendar(year)
      print(text)
    except ValueError:
      print("Try again")
      continue
  elif choice == 4:
    pass
  elif choice == 5:
    print ("See you!")
    break 