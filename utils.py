# from datetime import datetime
# def get_current_time():
#   return datetime.now()


# if __name__=="__main__":
#    print ("as a file, not main", get_current_time())

# annotations
from constans import SECOND_IN_MINUTE

def minutes_to_seconds(minutes: int) -> str:
  res: int = minutes*SECOND_IN_MINUTE
  return f"time is: {res}"



def minutes_to_miliseconds(minutes: int) -> str:
  res: int = minutes*SECOND_IN_MINUTE*1000
  return f"time is: {res}"

print("fjhsdkhjksdf")

if __name__ == "__main__":
    print(minutes_to_seconds(60))
    print(minutes_to_miliseconds(60))