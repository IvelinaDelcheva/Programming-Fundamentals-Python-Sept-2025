def urgent(groceries: list, urgent_item: str) -> list:
    if urgent_item not in groceries:
        groceries.insert(0, urgent_item)
    return groceries

def unnecessary (groceries: list, unnecessary_item: str) -> list:
    if unnecessary_item in groceries:
        groceries.remove(unnecessary_item)
    return groceries 


def correct(groceries: list, old_item: str, new_item: str) -> list:
    if old_item in groceries:
        old_item_index = groceries.index(old_item)
        groceries.remove(old_item)
        groceries.insert(old_item_index, new_item)
    return groceries 


def rearrange(groceries: list, rearrange_item: str) -> list:
    if rearrange_item in groceries:
        groceries.remove(rearrange_item)
        groceries.append(rearrange_item)
    return groceries


list_with_groceries = input().split('!') 
command = input()
while command != 'Go Shopping!':
        
    action = command.split(' ')[0]

    if action == 'Urgent':
        item = command.split(' ')[1]
        urgent(list_with_groceries, item)
    elif action == 'Unnecessary':
        item = command.split(' ')[1]
        unnecessary(list_with_groceries, item)
    elif action == 'Correct':
        old_item = command.split(' ')[1]
        new_item = command.split(' ')[2]
        correct(list_with_groceries, old_item, new_item)
    elif action == 'Rearrange':
        item = command.split(' ')[1]
        rearrange(list_with_groceries, item)
    command = input()

print(', '.join(list_with_groceries))


