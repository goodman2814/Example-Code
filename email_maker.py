from argparse import ArgumentParser
from datetime import date

parser = ArgumentParser()
parser.add_argument('-name') 
parser.add_argument('-email_date')

def main(name=None, email_date=None):
    if name is None:
        name = 'comrade'
    if email_date is None:
        email_date = date.today().strftime('%m-%d-%y')

    template = f'Hello {name},\n\n\nI hope you are doing well!\n\nIf you have a moment, please send me a cake by this date: {email_date}.\n\n\nCheers, A Cake Lover'

    # template = 'Hello {0},\n\nI hope you are doing well.\nIf you have a moment, please send me a cake by this date: {1}.\n\n\nCheers,\nA cake'.format(name, email_date)


    print('\n\n\n')
    print(template)
    print('\n\n\n')

if __name__ == "__main__":
    args = parser.parse_args()
    main(name=args.name, email_date=args.email_date)

