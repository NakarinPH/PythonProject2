from inventory_item import InventoryItem
from book import Book
from magazine import Magazine


def main():
    print('Start of Lab12P1')

    # Create objects
    book1 = InventoryItem('Bookmark', 250, 1.00)
    book2 = Book('Science Book', 100, 22.95, True)
    book3 = Book('Fiction Book', 150, 8.95, False)
    book4 = Magazine('Time', 75, 6.95, 447, 'Weekly')
    book5 = Magazine('Consumer Reports', 50, 5.95, 312, 'Monthly')

    # Create 3 additional objects by asking the user
    item_type = int(input('What item type (1-Book, 2-Magazine, 3-Other)? '))

    if item_type == 1:
        book6 = Book()
        book6.get_item_input()
    elif item_type == 2:
        book6 = Magazine()
        book6.get_item_input()
    else:
        book6 = InventoryItem()
        book6.get_item_input()

    item_type = int(input('What item type (1-Book, 2-Magazine, 3-Other)? '))

    if item_type == 1:
        book7 = Book()
        book7.get_item_input()
    elif item_type == 2:
        book7 = Magazine()
        book7.get_item_input()
    else:
        book7 = InventoryItem()
        book7.get_item_input()

    item_type = int(input('What item type (1-Book, 2-Magazine, 3-Other)? '))

    if item_type == 1:
        book8 = Book()
        book8.get_item_input()
    elif item_type == 2:
        book8 = Magazine()
        book8.get_item_input()
    else:
        book8 = InventoryItem()
        book8.get_item_input()

    # Display the objects
    print('Item 1: ', book1)
    print('Item 2: ', book2)
    print('Item 3: ', book3)
    print('Item 4: ', book4)
    print('Item 5: ', book5)
    print('Prompted items:')
    print(book6)
    print(book7)
    print(book8)


main()
