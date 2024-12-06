price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
q=0
w=0
for c,p in price_list.items():
    print(f'{c} {p}')
for p in price_list.values():
    q += p
print(f'{q: .2f}')
for c,p in price_list.items():
    p=p*0.9
    price_list[c]=int(p)
print(price_list)
for p  in price_list.values():
    w+=p
print(w)
