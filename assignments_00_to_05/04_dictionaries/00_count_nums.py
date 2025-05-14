blue_start = '\033[34m'
blue_end = '\033[0m'

def get_user_numbers():
    numbers = []
    while (num := input(f"{blue_start}Enter a number: {blue_end}")) != "":
        numbers.append(int(num))
    return numbers

def count_nums(lst):
    unique = set(lst)
    return {num: lst.count(num) for num in unique}

def print_counts(counts):
    for k, v in counts.items():
        print(f"{k} appears {v} times.")

if __name__ == "__main__":
    print_counts(count_nums(get_user_numbers()))
