import random


def get_numbers():
    numbers_list = []
    for i in range(10):
        numbers_list.append(i)
    numbers_lottery = random.sample(numbers_list, k=7)
    return numbers_lottery


def main():
    get_numbers()
    print('The lottery number is:')
    for num in get_numbers():
        print(num, end='')


if __name__ == '__main__':
    main()

