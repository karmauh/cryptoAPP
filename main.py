from coinbaseExchange import CoinbaseExchange
from datetime  import datetime
from sys import exit


if __name__ == '__main__':
    coinbase = CoinbaseExchange()

    print('\
        What you would like to do:\n\
        1 - show all available pairs.\n\
        2 - check today\'s currency price. \n\
        3 - check the price of the currency on the given day and time.\n\
        4 - compare the purchase price to today\'s valuation.\n\
        n - Exit.    \n\
        ')

    choice = input('Your choice is? ')

    match choice:
        case '1':
            coinbase.all_pairs()
        case '2':
            currency_pair = input('Name the currency pair (e.g. BTC-USD): ')
            
            coinbase.get_price(currency_pair)
        case '3':
            currency_pair = input('Name the currency pair (e.g. BTC-USD): ')
            purchase_date = input('Enter the date of purchase in the format YYYY-MM-DD: ')
            purchase_time = input('Enter the time of purchase in HH:MM format: ')
            
            purchase_datetime = datetime.strptime(f'{purchase_date} {purchase_time}', '%Y-%m-%d %H:%M')
            
            coinbase.get_price(currency_pair, purchase_datetime)
        case '4':
            currency_pair = input('Name the currency pair (e.g. BTC-USD): ')
            retail = float(input('Retail: '))
            
            coinbase.compare_prices(currency_pair, retail)
            
        case 'n':
            exit()
        case _:
            print('Wrong number.')