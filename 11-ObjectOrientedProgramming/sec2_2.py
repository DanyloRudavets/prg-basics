# class definition
class Song:
   def __init__(self,artist: str,tracktitle: str,album: str,year: str):
        self.artist= artist
        self.tracktitle= tracktitle
        self.album= album
        self.year= year
   def __str__(self):
        return f'Performer: {self.artist} \n Title: {self.tracktitle} \n Album: {self.album} \n Year: {self.year}'
   

# object creation
song1 = Song('Ed Sheeran','Hearts Don\'t Break Around Here', 'Divide',  '2017')
song2 = Song('Queen','Bohemian Rhapsody', 'A Night at the Opera', '1975')

## object usage
print(song1)
print(song2)