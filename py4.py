string_good = input('Enter your goods with separated by commas:')

goods = [x.strip() for x in string_good.split(',')]

search = input('search: ')

if search in goods:
    print("Available")
else:
    print("Out of stock!")