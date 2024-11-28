computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
i=0
c=sorted(computer_games)
for x in c:
    print(x)
while i<len(computer_games):
    i+=1
    computer_games.sort()
    print(i, end=' ')
    print(computer_games[i-1])
