def get_store_sales():
    sales = []
    entry = 0.0
    for day in range(7):
        entry = float(input(f'Enter the sales amount for day #{day + 1}: '))
        sales.append(entry)
    return sales


def total_sales(sales_list):
    total = 0.0
    for sale in sales_list:
        total += sale
    return total


def itemize_sales(sales_list):
    print('The list of sales for the week:')
    print('---------------')
    for i in range(len(sales_list)):
        print(f'Day {i + 1}: ${sales_list[i]}')


def main():
    sales_list = get_store_sales()
    itemize_sales(sales_list)
    total = total_sales(sales_list)
    print(f'The total sales for the week is ${total:.2f}')


if __name__ == '__main__':
    main()
