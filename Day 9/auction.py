import os


def clear_screen():
    """
    A function to clear the screen when required. Works in Terminal only.
    :return:
    """
    os.system('clear')


def get_bidder_input():
    """
    Function to get user inputs
    :return: Bidder name and his price
    """
    try:
        name = input('What is your name?\n').title().strip()
        bid = int(input('What is your bid? $'))
        return name, bid
    except ValueError:
        print('Invalid input. Please enter a valid bid.')
        return get_bidder_input()


def check_progress():
    """
    Function to check if auction continues or must be stopped.
    :return:
    """
    while True:
        answer = input('Are there any other participants? "yes" or "no"\n').lower().strip()
        if answer in ['yes', 'no']:
            clear_screen()
            return answer
        else:
            print('Wrong input. Try again')


def main():
    auction = []

    while True:
        name, bid = get_bidder_input()
        auction.append({'name': name, 'bid': bid})
        if check_progress() == 'no':
            break

    if auction:
        # finding the max bid value in the dictionaries of the auction list. Returns the dictionary containing
        # the actual max value of the bid:
        max_bidder = max(auction, key=lambda x: x['bid'])
        print(f'This auction was won by {max_bidder["name"]} with a bid of ${max_bidder["bid"]:.2f}')
    else:
        print("No valid bids received. Auction failed.")


if __name__ == '__main__':
    main()
