#2 lists
#list1: 5 syllables
#list2: 7 syllables         
#5,7,5
#print 3 haikus (line in between)

import random 

fiveSyllables = ["Fat man sees small door", "Haikus are easy", "Love is very tough", "Buds blooming in May", "Falling to the ground", "As the wind does blow"]
sevenSyllables = ["Met 3 silver spoons last night", "Balancing its tomato", "I go cuckoo for cocoa"]


for i in range(3):
    print (fiveSyllables[random.randint(0,len(fiveSyllables) -1)] + "\n" +
           sevenSyllables[random.randint(0,len(sevenSyllables)-1)] + "\n" + fiveSyllables[random.randint(0,len(fiveSyllables) -1)] + "\n" + "\n")
     
    
    
        
