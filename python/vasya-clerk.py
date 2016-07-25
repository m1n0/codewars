// https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8
def tickets(people):
    print (people)
    price = 25
    change = {
        25: 0,
        50: 0,
        100: 0,
    }

    for payment in people:
        if (payment == price):
            change[payment] += 1
        else:
            change[payment] += 1

            if (payment == 50 and change[25] < 1): return "NO"
            elif (payment == 50): change[25] -= 1

            if (payment == 100 and ((change[25] < 1 or change[50] < 1) and change[25] < 3)): return "NO"
            elif(payment == 100):
                if (change[50] > 0 and change[25] > 1): change[25] -= 1; change[50] -= 1
                elif (change[25] >= 3): change[25] -= 3

    return "YES"
