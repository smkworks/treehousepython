__author__ = 'seanknowles'

shopping_list = list()

print("what should we pick up at the store?:")
print("Enter 'DONE' to exit and stop adding items to your list!")

while True:
    new_item = input("> ")

    if new_item == "DONE":
        break

    if new_item == "done":
        break

    shopping_list.append(new_item)
    print("Added! List has {} items.".format(len(shopping_list)))
    continue

print("Here's your new shopping list:")

for item in shopping_list:
    print(item + ",")






