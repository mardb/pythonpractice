
shopping_list = []

def show_help():
  print("What should we pick up at the store?")
  print("""
  Enter 'DONE' to stop adding items. 
  Enter 'HELP' for this help.
  Enter 'SHOW' to see your current list.
  """)
  

def add_to_list(item):
  shopping_list.append(item)
  print("Added! List has {} items.".format(len(shopping_list)))

# define a  new fn called show list  that prints all items in the list 
def show_list():
  print("Here is your list:")
  for item in shopping_list:
    print(item)

show_help()
while True: 
  new_item = input("> ")

  if new_item == 'DONE':
    break
  elif new_item == 'HELP':
    continue
  elif new_item == 'SHOW':
    show_help()
    continue
    # enable the show command. 
  # HINT: make sure to run  it
  show_list()
  add_to_list(new_item)

show_list()