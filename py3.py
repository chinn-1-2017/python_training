import math


def checkLeg(leg1, leg2):
    try:
        float(leg1)
        float(leg2)
        return True
    except Exception as e:
        return False


leg1 = 0
leg2 = 0

while True:
    leg1 = input('Leg1: ')
    leg2 = input('Leg2: ')
    if checkLeg(leg1, leg2):
        leg1 = float(leg1)
        leg2 = float(leg2)
        break
    print('Invalid, try again: ')

hypotenuse = math.sqrt(leg1 * leg1 + leg2 * leg2)

area = (leg1 * leg2) / 2

print("hypotenuse: ", hypotenuse)
print("area: ", area)
