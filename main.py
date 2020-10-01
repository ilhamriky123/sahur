import pytz
from datetime import datetime
import os

jamSahur = str(input("Setting Jam Sahur: "))
hh = str(input("Klik 1: "))

print ("\n", end = '')
while True:
  time_indonesia = pytz.timezone('Asia/Jakarta')
  datetime_indonesia = datetime.now(time_indonesia)
  if str(jamSahur) == datetime_indonesia.strftime("%H:%M"):
    while True:
      if "2" in hh:
        from playsound import playsound
        print ("\nSahuurrrrr Baangggggg!...", end = '')
        print ("\nPlaying Alarm Sahur 1...", end = '')
        playsound('vids/sahur1.mp3')
        print ("\nPlaying Alarm Sahur 2...", end = '')
        playsound('vids/sahur3.mp3')
        print ("\nPlaying Alarm Sahur 3...", end = '')
        playsound('vids/sahur2.mp3')
        print ("\nPlaying Alarm Sahur 3...", end = '')
        playsound('vids/sahur2.mp3')
      elif "1" in hh:
        print ("\nWaktunya Sahuurrrrr Gaannn!...", end = '')
        print ("\nPlaying Alarm Sahur 1...", end = '')
        os.system('mpv vids/sahur1.mp3')
        print ("\nPlaying Alarm Sahur 2...", end = '')
        os.system('mpv vids/sahur3.mp3')
        print ("\nPlaying Alarm Sahur 3...", end = '')
        os.system('mpv vids/sahur2.mp3')  
  else:
    print("\rBelum Waktunya Sahur Brooo... Jam Sekarang:", datetime_indonesia.strftime("%H:%M:%S"), end = '')
