"""Call detweeter modules."""


from __future__ import print_function
from tweet_reader import twit_reader


twits = twit_reader()

for twit in twits:
    print (twit)
