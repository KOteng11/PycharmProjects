def main():
    items = get_items("Item: ")
    display(format_items(items))


def display(items):
    for each_item in items:
        print(f"{items[each_item]} {each_item}")


def format_items(groceries):
    dict_groceries = {}
    for each_item in groceries:
        count = groceries.count(each_item)
        dict_groceries[each_item] = count
    return dict_groceries


def get_items(prompt):
    list_of_items = []
    while True:
        item = input(prompt).lower()
        if item == "control-d":
            return list_of_items
        else:
            list_of_items.append(item.upper())
            list_of_items.sort()


main()
