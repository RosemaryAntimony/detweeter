"""Call detweeter modules."""


from __future__ import print_function
import imaginations as imags
import markovify
import os
# import run_the_jewels as rtj
import sys as trans
import tweepy
import tweet_reader as tr


year = "2017"
month = "6"
day = "1"
if len(trans.argv) > 4:
    year = trans.argv[2]
    month = trans.argv[3]
    day = trans.argv[4]
if len(trans.argv) > 1:
    user = trans.argv[1]
else:
    user = "realdonaldtrump"


keys = tr.key_access()
auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth)

path = "twits/imgs/" + user + "/"
if not os.path.exists(path):
    os.makedirs(path)

path = "twits/" + user + "/"
if not os.path.exists(path):
    os.makedirs(path)


os.system("python scrape.py " + user + " " + year + " " + month + " " + day)
os.system("python get_metadata.py " + user)

profile = api.get_user(user)
pic_add = profile.profile_image_url
pic = imags.get_twitpic(pic_add.replace("_normal", ""), user)
pix = pic.load()
path = "/home/lucifer/Documents/snek/scribbles/detweeter"\
       + "/twits/imgs/" + user + '/'

data = tr.twit_reader(user)

with open("./twits/corpses/" + user + "_corpus.txt", "w") as fp:
    for ii in range(len(data)):
        for obj in reversed(data[ii]):
            twit = obj["text"] + "\n"
            fp.write(twit.encode("utf-8"))

with open("./twits/corpses/" + user + "_corpus.txt", 'r') as cf:
    corpus = cf.read()

    model = markovify.Text(corpus)

tweet_len = 138 - len(user)
sentence = ''
temp_sentence = model.make_short_sentence(tweet_len)
if temp_sentence is not None:
    sentence += temp_sentence
    tweet_len -= len(temp_sentence) + 1

while len(sentence) < 100:
    temp_sentence = model.make_short_sentence(tweet_len)
    if temp_sentence is not None:
        sentence += ' ' + temp_sentence
        tweet_len -= len(temp_sentence) + 1

sentence += " #" + user
pic_name = user + "_test_tw_circplus_01.jpg"
xx = pic.size[0]
yy = pic.size[1]

temp_sentence = model.make_short_sentence(72)
while temp_sentence is None:
    temp_sentence = model.make_short_sentence(72)
while len(temp_sentence) < 46:
    temp_temp = model.make_short_sentence(60)
    if temp_temp is not None:
        temp_sentence += " " + temp_temp

l1 = temp_sentence[0:16]
l2 = temp_sentence[16:32]
l3 = temp_sentence[32:48]

imags.xorror(pix, xx, yy, sentence)
imags.shapes(pix, xx, yy, sentence,
             (ord(sentence[66]) / 8) % len(sentence) + 1)
imags.wordler(pic, l1, l2, l3)
imags.scoots(pix, xx, yy, sentence)
imags.xorror(pix, xx, yy, sentence)
pic.save(path + pic_name)

sentence = sentence.replace("@", "#")
sentence = sentence.replace("&amp;", "&")
print (sentence)

try:
    api.update_with_media(path + pic_name, sentence)
except Exception:
    print("You're still banned, idiot.")

try:
    os.remove(user + ".csv")
except Exception:
    print ("Okay")

try:
    os.remove(user + ".zip")
except Exception:
    print ("bye")
