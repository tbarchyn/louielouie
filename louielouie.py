import time
import random

lyrics = ['Louie Louie, oh no',
'Me gotta go',
'Aye-yi-yi-yi, I said',
'Louie Louie, oh baby',
'Me gotta go',
'Fine little girl waits for me',
'Catch a ship across the sea',
'Sail that ship about, all alone',
'Never know if I make it home',
'Louie Louie, oh oh no',
'Me gotta go, oh no',
'Louie Louie, oh baby',
'I said we gotta go',
'Three nights and days I sail the sea',
'Think of girl, constantly',
'On that ship, I dream shes there',
'I smell the rose in her hair.',
'Louie Louie, oh no',
'Me gotta go',
'Aye-yi-yi-yi, I said',
'Louie Louie, oh baby',
'Me gotta go',
'Okay, lets give it to em, right now!',
'See Jamaica, the moon above',
'It wont be long, me see me love',
'Take her in my arms again',
'I tell her Ill never leave again',
'Louie Louie, oh no',
'Me gotta go',
'Aye-yi-yi-yi, I said',
'Louie Louie, oh baby',
'Me gotta go',
'I said we gotta go now',
'Lets take it on outta here now',
'Lets go!']

for lyric in lyrics:
    print (lyric)
    nap = random.weibullvariate (4, 1)
    time.sleep (nap)
    
