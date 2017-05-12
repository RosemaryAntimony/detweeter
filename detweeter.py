"""Call detweeter modules."""


from __future__ import print_function
import tweet_reader as tr

twits = tr.twit_reader()

longth = 0
for twit in twits:
    longth += len(twit)

print ("all " + str(len(twits)) + " twits are " + str(longth) + " longed")
