# tv.py file
# class definition
class TV:
   def __init__(self):
      self.is_on = False
      self.channel_no=1
      self.channels_list=[]
      self.volume=0
   def turn_off(self):
       self.is_on=False
       return self.is_on
   def turn_on(self):
        self.is_on=True
        return self.is_on
   def show_status(self):
        if self.is_on==True:
            return f'{self.is_on}, channel {self.channel_no} ({self.channels_list[self.channel_no-1]}) volume {self.volume}'
        else:
            return self.is_on
   def channel_no(self, number):
       self.channel_no=number
       return self.channel_no
   def set_channels(self,channels_list):
       self.channels_list.append(channels_list)
       return self.channels_list
   def show_channels(self):
       return self.channels_list
   def inc_volume(self):
        if self.volume<10:
            self.volume+=1
            return self.volume
   def dec_volume(self):
       if self.volume>0:
            self.volume-=1
            return self.volume
       
       
       