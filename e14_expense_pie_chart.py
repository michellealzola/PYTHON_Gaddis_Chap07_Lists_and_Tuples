import matplotlib.pyplot as plt


def main():
    slice_labels = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']
    expenses = []
    for i in range(len(slice_labels)):
        expenses.append(float(input(f'Enter expense for {slice_labels[i]}: ')))

    plt.pie(expenses, labels=slice_labels, colors=('y', 'g', 'm', 'c', 'b', 'r'))
    plt.title('Expenses')
    plt.show()


if __name__ == '__main__':
    main()
