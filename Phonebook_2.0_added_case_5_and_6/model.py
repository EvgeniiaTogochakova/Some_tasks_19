phone_book: list[dict[str, str]] = []
path = 'phone.txt'


def open_pb():
    global phone_book, path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = [i.strip() for i in contact.split(':')]
        if len(contact) == 3:
            phone_book.append({'name': contact[0], 'phone': contact[1], 'comment': contact[2]})


def save_pb():
    data = []
    for contact in phone_book:
        contact = ':'.join([value for value in contact.values()])
        data.append(contact)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(data))


def get_pb() -> list[dict[str, str]]:
    global phone_book
    return phone_book


def add_contact(contact: dict[str, str]):
    global phone_book
    phone_book.append(contact)
    return contact.get('name')


def del_contact(index: int):
    return phone_book.pop(index - 1).get('name')


def find_contact(to_find: str) -> dict:
    global phone_book
    if to_find:
        for contact in phone_book:
            if to_find in contact.get("name"):
                return contact


def change_contact(a: bool, contact1: dict[str, str], contact2: dict[str, str], path):
    global phone_book
    if a:
        new_list = []
        for contact in phone_book:
            if contact != contact1:
                new_list.append(":".join((contact['name'], contact['phone'], contact['comment'])))
            else:
                new_list.append(":".join((contact2['name'], contact2['phone'], contact2['comment'])))
        with open(path, 'w', encoding='utf-8') as file:
            for i in new_list:
                file.write(i + '\n')
