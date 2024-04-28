lis = []
lis2 = []
lis3 = []
tax = 0

def get_spaces(str):
    spaces = ''
    space_range = 30 - len(str)
    for s in range(space_range):
        spaces += ' '
    return spaces    
    

def Item_Name():
    i = True
    while i == True:
        x = input('Enter the name for the item: ')
        if x == '':
            i = False
            break
        lis.append(x.lower())

def Item_Price():
    for i in range(len(lis)):
        price = float(input(f'Enter the price for {lis[i]}: '))
        lis2.append(price)


def Item_Tax(tax):
    a = True
    while a == True:
        Tax_Item = str(input('Enter the item which is taxable: '))
        if Tax_Item == '':
            a = False
        else:
            for i in range(len(lis)):
                if lis[i] == Tax_Item.lower():
                    Tax_Price = lis2[i] * 0.15
                    tax += Tax_Price
                    lis3.append(Tax_Item.lower())

    Sub_Total = sum(lis2)
    Total = Sub_Total + tax

    print('==============================') 
    print('Receipt')
    print('------------------------------')
    for i in range(len(lis)):
        t = ' '
        if lis[i] in lis3:
            t = 'T'    
        item = lis[i]
        price = f'{lis2[i]} {t}'
        spaces = get_spaces(f'{item}{price}')
        x = f'{item.capitalize()}{spaces}{price}'
        print(x)

    print('------------------------------')
    
    print('Subtotal ' + get_spaces('Subtotal ' + str(Sub_Total) + '  ') + str(Sub_Total))    
    print('------------------------------')
    
    print('Tax ' + get_spaces('Tax ' + str(round(tax,2)) + '  ') + str(round(tax,2)))
    print('Total ' + get_spaces('Total ' + str(round(Total,2))  + '  ') + str(round(Total,2)))   
    print('==============================') 


Item_Name()
Item_Price()
Item_Tax(0)
