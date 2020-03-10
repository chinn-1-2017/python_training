def checkTem(number):
    try:
        float(number)
        return True
    except Exception as e:
        return False


while True:
    tem = input('Temperature (°C): ')
    if checkTem(tem):
        tem = float(tem)
        break
    print('Invalid, please enter again: ')

temInF = (tem * 9 / 5) + 32

print('Temperature (°F): ', temInF)
