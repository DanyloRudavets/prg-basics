
medal_data = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7},
]
j=filter(lambda x: x['gold']+x['silver']+ x['bronze']>=10, medal_data)
for i in j:
    medals= [i['gold'], i['silver'], i['bronze']]
    print(f"{i['country']}: {list(map(lambda x: x, medals))}")
