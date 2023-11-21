import time

def count_typing_speed():

  start_time = time.time()
  user_input = input("Type something: ")
  end_time = time.time()
  typing_time = end_time - start_time
  number_of_words = len(user_input.split())
  typing_speed = number_of_words / typing_time * 60

  print("Your typing speed is {} words per minute.".format(typing_speed))

if __name__ == "__main__":
  count_typing_speed()