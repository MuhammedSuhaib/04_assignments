def read_phone_numbers():
    phone_book = {}
    while (name := input("Name: ")):
        phone_book[name] = input("Number: ")
    return phone_book

def print_phone_book(phone_book):
    for name, number in phone_book.items():
        print(f"{name} -> {number}")

def lookup_numbers(phone_book):
    while (name := input("Enter name to lookup: ")):
        print(phone_book.get(name, f"{name} is not in the phonebook"))

def main():
    phone_book = read_phone_numbers()
    print_phone_book(phone_book)
    lookup_numbers(phone_book)

if __name__ == '__main__':
    main()
