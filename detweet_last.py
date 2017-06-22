"""Check for new twits."""
import detweet as dtw
import imaginations as imags
import json
from run_the_jewels import listicle
import time
import tweepy
import tweet_reader as tr


def jewel_runner():
    """Run the jewels."""
    for item in listicle:
        try:
            new_twit = api.user_timeline(item)[0].text
            print("checking " + item)
            if new_twit != twit_dic[item]:
                print(" gotcha")
                dtw.detweet(item)
                twit_dic[item] = new_twit
                with open("recent_twits.json", "w") as fn:
                    json.dump(twit_dic, fn)
                break
        except Exception:
            try:
                twit = api.user_timeline(item)[0].text
                twit_dic.update({item: twit})
            except Exception:
                print("maybe delete {}, grrrl".format(item))


def mangle_reply(tweet):
    """Mangle a reply to a tweet."""
    user = tweet.screen_name
    t_id = tweet.id
    words = tweet.text

    while len(words) < 100:
        words += words

    profile = api.get_user(user)
    pic_add = profile.profile_image_url
    pic = imags.get_twitpic(pic_add.replace("_normal", ""), user)
    pix = pic.load()
    xx = pic.size[0]
    yy = pic.size[1]

    l1 = words[0:16]
    l2 = words[16:32]
    l3 = words[32:48]

    imags.xorror(pix, xx, yy, words)
    imags.shapes(pix, xx, yy, words,
                 (ord(words[66]) / 8) % len(words) + 1)
    imags.wordler(pic, l1, l2, l3)
    imags.scoots(pix, xx, yy, words)
    imags.xorror(pix, xx, yy, words)

    path = "./twits/imgs/temp.jpg"
    pic.save(path)
    twit = "@" + user + ", I love you with all of my cold, robot heart"
    api.update_with_media(path, twit, in_reply_to_status_id=t_id)


keys = tr.key_access()
auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth)

try:
    with open("recent_twits.json") as fn:
        twit_dic = json.load(fn)
except Exception:
    with open("recent_twits.json", "w") as fn:
        twit_dic = {}

if not len(twit_dic):
    print("dick")
    for item in listicle:
        try:
            twit = api.user_timeline(item)[0].text
            twit_dic.update({item: twit})
            print(item + ': ' + twit)
        except Exception:
            "That one don't exist, babe."
    with open("recent_twits.json", "w") as fn:
        json.dump(twit_dic, fn)
naps = 0
while(True):
    naps += 1
    try:
        for mentos in api.mention(count=5):
            mangle_reply(mentos)
    except Exception:
        print("You ain't that popular, babe")
    try:
        jewel_runner()
        print(" naptime babez " + str(naps))
        time.sleep(30)
    except Exception:
        print("UNICODE")
