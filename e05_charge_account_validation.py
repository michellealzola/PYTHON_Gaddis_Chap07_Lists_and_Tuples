def verify_account(acct_number):
    infile = open('charge_accounts.txt', 'r')
    accounts = infile.readlines()
    infile.close()

    for index in range(len(accounts)):
        accounts[index] = accounts[index].rstrip('\n')

    is_valid = False
    if acct_number in accounts:
        is_valid = True
    else:
        is_valid = False

    return is_valid


def main():
    acct_number = input('Enter your account number: ')
    if verify_account(acct_number):
        print('The account is valid')
    else:
        print('The account is INVALID')


if __name__ == '__main__':
    main()
