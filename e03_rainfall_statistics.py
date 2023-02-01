import matplotlib.pyplot as plt

NUM_MONTHS = 12


def get_rainfall_list():
    rainfall_list = []
    print('Enter the amount of rainfall for the following months')
    for month in range(NUM_MONTHS):
        amount = float(input(f'Month {month + 1}: '))
        rainfall_list.append(amount)
    return rainfall_list


def get_total_rainfall(rainfall_list):
    total = 0.0
    for amount in rainfall_list:
        total += amount
    return total


def get_average_rainfall(total_rainfall):
    average = total_rainfall / NUM_MONTHS
    return average


def get_month_highest(rainfall_list):
    highest = max(rainfall_list)
    month_index = rainfall_list.index(highest)
    return month_index + 1


def get_month_lowest(rainfall_list):
    lowest = min(rainfall_list)
    month_index = rainfall_list.index(lowest)
    return month_index + 1


def get_bar_chart(rainfall_list):
    x_values = []
    for num in range(NUM_MONTHS):
        x_values.append(num + 1)
    y_values = []
    for values in rainfall_list:
        y_values.append(values)
    bar_width = .5
    plt.bar(x_values, y_values, bar_width)

    plt.title('Amount of Rainfall')
    plt.xlabel('Months')
    plt.ylabel('Rainfall')

    plt.xticks(x_values, x_values)

    plt.show()


def get_actual_month(month_number):
    if month_number == 1:
        month = 'January'
    elif month_number == 2:
        month = 'February'
    elif month_number == 3:
        month = 'March'
    elif month_number == 4:
        month = 'April'
    elif month_number == 5:
        month = 'May'
    elif month_number == 6:
        month = 'June'
    elif month_number == 7:
        month = 'July'
    elif month_number == 8:
        month = 'August'
    elif month_number == 9:
        month = 'September'
    elif month_number == 10:
        month = 'October'
    elif month_number == 11:
        month = 'November'
    else:
        month = 'December'
    return month


def main():
    rainfall_list = get_rainfall_list()
    print('The rainfall list ', rainfall_list)
    total_rainfall = get_total_rainfall(rainfall_list)
    print(f'The total rainfall for the year is {total_rainfall:.2f}')
    average_rainfall = get_average_rainfall(total_rainfall)
    print(f'The average rainfall for the year is {average_rainfall:.2f}')
    highest_month = get_month_highest(rainfall_list)
    month = get_actual_month(highest_month)
    print(f'The month with the highest rainfall is {month}')
    lowest_month = get_month_lowest(rainfall_list)
    month = get_actual_month(lowest_month)
    print(f'The month with the lowest rainfall is {month}')
    get_bar_chart(rainfall_list)


if __name__ == '__main__':
    main()
