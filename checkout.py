"""
Check out at the cashier. Conditional is used to
change flow control out of the loop and total up
your items for purchase.
Thank you, come again, please!

"""

def checkout():
    total = 0
    count = 0
    moreItems = True

    while moreItems:
        price = float(input('Enter item price (0 when done): '))
        if price != 0:
            count += 1
            total += price
            print('Subtotal: €', round(total, 2))
        elif price < 0:
            #total += price
            print('Do you need a mgr approval?')
            print('Subtotal: €', round(total, 2))
        else:
            moreItems = False
        avg = total / count


    print('Total items:', count)
    print('Total €', round(total, 2))
    print('Avg price/item: €', round(avg, 2))


def main():
    checkout()

if __name__ == '__main__':
    main()
