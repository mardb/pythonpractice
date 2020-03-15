# create a new empty list called shopping list
shopping_list = []
#create a fn named add to list that declares a parameter named item 
def add_to_list(item):
  #add the item to the list
  shopping_list.append(item)
  # notify the user that the item was added and state the number of items in the current list
  print("Added! List has {} items.".format(len(shopping_list)))


def show_help():
  print("What should we pick up at the store?")
  print("""
  Enter 'DONE' to stop adding items. 
  Enter 'HELP' for this help
  """)
  
show_help()
while True: 
  new_item = input("> ")

  if new_item == 'DONE':
    break
  elif new_item == 'HELP':
    show_help()
    continue
    # call add_to_list with new item as an argument
    add_to_list(new_item)
