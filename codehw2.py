from microbit import *
import random
import time
import music

#Project update 04/23/20 Kimie (Pei-Chun) Ou Yang
#Please connect your buzzer to listen to music!
#1.Display fortune teller machin instruction (temp on LED for now)
#2.An asker input frmo sensor (temp on the micro bit light and accelerometer sensor for now)
#3.Display "loading graphes" as the universe is receiving the asker's question (temp on the micro bit LED)
#4.Press btn to finish the asking
#5.Random display a positive msg from system msg set with a random song in the background(temp on the micro bit LED) 



#setup
msgs = ["You got this!", 
        "The universe is listening to you", 
        "Trust yourself!", 
        "You are loved", 
        "The best is yet to come", 
        "Follow your heart", 
        "Stay strong" ]
#These msgs are temp, I would look for more msgs that meet the standard I mentioned in my proposal 

song_list = [music.PRELUDE, music.NYAN, music.PYTHON, music.CHASE]
arrow_image_list = [Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW]
#another animate img setup 
pattern1 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "99999")

pattern2 = Image("00000:"
              "00000:"
              "00000:"
              "99999:"
              "99999")

pattern3 = Image("00000:"
              "00000:"
              "99999:"
              "99999:"
              "99999")

pattern4 = Image("00000:"
              "99999:"
              "99999:"
              "99999:"
              "99999")

pattern5 = Image("99999:"
              "99999:"
              "99999:"
              "99999:"
              "99999")

pattern6 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")
all_patterns = [pattern1, pattern2, pattern3, pattern4, pattern5, pattern6]

#intro
display.show(Image.HAPPY)
sleep(2000)
display.scroll('cover & shake board while asking question', delay=100)
display.scroll('press any btn to finish asking', delay=100)
#I tried to use the "while not" to include the intro in the loop inside the while ture but failed 
while True:
    was_shook = accelerometer.was_gesture("shake")
    is_low_light = display.read_light_level() < 20
    any_button = button_a.is_pressed() or button_b.is_pressed()
    if was_shook and is_low_light:
        #cover and shake the board to start the asking process like just like hold hands to ask with eyes closed
        #and sometimes the light sensor is too sensitive, don't know how to make it not so sensitive
        display.show(arrow_image_list)
        display.show(all_patterns, loop=True, delay=600, wait=False)
    if any_button:    
        #press to finish asking
        time.sleep(1)
        #show animated image as the loading indicator 
        display.scroll(random.choice(msgs), wait=False) 
        #show the random positice msg to the asker
        music.play(random.choice(song_list))
        #play a random song to cheer up the asker
        display.show(Image.HAPPY)
        sleep(2000)
        #indicate the process is done
