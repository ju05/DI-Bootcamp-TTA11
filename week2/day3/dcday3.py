items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"
clean_wallet = int(wallet.strip('$'))

clean_items_purchase = {}

for item, price in items_purchase.items():
    clean_price = price.strip('$')
    clean_price = clean_price.replace(',', '')
    clean_price = float(clean_price)
    clean_items_purchase.update({item : clean_price})

print(clean_items_purchase)

# check the price
# compare/ check if I have enough money for it
# put the item in the basket
# subtract the price from my wallet

basket= []

for item, price in clean_items_purchase.items(): # check the price
    if price <= clean_wallet: # compare/ check if I have enough money for it
        basket.append(item) # put the item in the basket
        clean_wallet -= price
    else:
        continue

print(basket)



