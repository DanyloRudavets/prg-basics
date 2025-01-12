# tv_show.py file
# main program
import sec3_1
from sec3_1 import TV

def main():
   tv1=sec3_1.TV()

   # object usage
   TV.turn_on(tv1)
   TV.channel_no(tv1,4)
   TV.set_channels(tv1,'TVP1')
   TV.set_channels(tv1,'TVP2')
   TV.set_channels(tv1,'Polsat')
   TV.set_channels(tv1,'TVN')
   TV.set_channels(tv1,'Filmbox')
   TV.set_channels(tv1,'Discovery')
   print(TV.show_channels(tv1))
   print(TV.show_status(tv1))
   TV.inc_volume(tv1)
   print(TV.show_status(tv1))


   

if __name__ == "__main__":
   main() 