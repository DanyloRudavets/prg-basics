hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    c=[]
    for i in hotels:
        c.append(i['name'])
    return c
def avg_price(hotels):
    p=0
    for i in hotels:
            p+=i['price']
    return p
def hotel_list1(hotels):
    c=[]
    for i in hotels:
        c.append(i['name'])
    return c
def avg_price1(hotels):
    p=0
    for i in hotels:
            p+=i['price']
    return p
print(hotel_list(hotels_in_Krakow))
print(avg_price(hotels_in_Krakow))
print(hotel_list1(hotels_in_Sopot))
print(avg_price1(hotels_in_Sopot))
