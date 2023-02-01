import matplotlib.pyplot as plt


def main():
    infile = open('1994_Weekly_Gas_Averages.txt', 'r')
    weekly_gas_list = infile.readlines()
    infile.close()
    for i in range(len(weekly_gas_list)):
        weekly_gas_list[i] = float(weekly_gas_list[i].rstrip('\n'))
    # print(weekly_gas_list)
    x_values = []
    for num in range(len(weekly_gas_list)):
        x_values.append(num + 1)

    plt.bar(x_values, weekly_gas_list)
    plt.title('1994 Weekly Gas Graph')
    plt.xlabel('Week Number')
    plt.ylabel('Average Gas Price per Week')

    plt.show()


if __name__ == '__main__':
    main()
