#Typing speed test

import time
import math
correct,incorrect = 0,0

print("Start typing when the timer ends")

timer = 5
while timer > 0:
    print(timer)
    time.sleep(1)
    timer-=1
    
t1 = time.time()
sentence = input("Click enter when you're done !! \n")
t2 = time.time()

sentence_list = sentence.split()

from autocorrect import Speller

spell = Speller(lang='en')

for word in sentence_list:
    if spell(word) == word:
        correct += 1
    else:
        incorrect +=1   

speed = (len(sentence_list) * 60)/(t2-t1)

if len(sentence) == 0:
    print("You haven't entered anything")
else:
    print("You have typed total",len(sentence_list),"words in",math.floor(t2-t1),"sec")
    print("Your typing speed is",math.floor(speed),"WPM")
    print("Incorrect words",incorrect)
    print("Correct words",correct)
    print("Accuracy",correct/(incorrect+correct) * 100,"%")
