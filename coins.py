coins = [5, 10, 25]
coins_inserted = 0
while coins_inserted< 50:
    inserting = int(input('Enter a coin one at a time: '))
    if inserting in coins:
        coins_inserted += inserting
    else:
        print('invalid coins')
if coins ==50:
    print('purchase is successful')
else:
    print(f"we owe you {coins_inserted-50} cents")
