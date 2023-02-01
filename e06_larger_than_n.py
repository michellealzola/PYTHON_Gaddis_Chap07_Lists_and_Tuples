def is_larger(number):
    infile = open('numberlist.txt', 'r')
    number_list = infile.readlines()
    infile.close()
    for i in range(len(number_list)):
        number_list[i] = int(number_list[i].rstrip('\n'))
    new_list_with_larger = []
    for num in number_list:
        if num > number:
            new_list_with_larger.append(num)

    return new_list_with_larger


def main():
    number = int(input('Enter a number from 0 - 10: '))
    print(f'The values greater than {number}: {is_larger(number)}')


if __name__ == '__main__':
    main()
