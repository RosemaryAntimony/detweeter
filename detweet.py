"""Make a detweet module."""
import imaginations as imags
import markovify
import tweepy
import tweet_reader as tr


def detweet(tweeter):
    """Detweet at someone."""
    keys = tr.key_access()
    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    api = tweepy.API(auth)

    profile = api.get_user(tweeter)
    pic_add = profile.profile_image_url
    pic = imags.get_twitpic(pic_add.replace("_normal", ""), tweeter)
    pix = pic.load()
    path = "./twits/imgs/" + tweeter + '/'

    data = tr.twit_reader(tweeter)

    with open("./twits/corpses/" + tweeter + "_corpus.txt", "w") as fp:
        for ii in xrange(len(data) if len(data) < 5000 else 5000):
            for obj in data[ii]:
                twit = obj["text"] + "\n"
                fp.write(twit.encode("utf-8"))

    with open("./twits/corpses/" + tweeter + "_corpus.txt", 'r') as cf:
        corpus = cf.read()

        model = markovify.Text(corpus, state_size=2)

    tweet_len = 138 - len(tweeter)
    sentence = ''
    temp_sentence = model.make_short_sentence(tweet_len, tries=10)
    while temp_sentence is None:
        temp_sentence = model.make_short_sentence(tweet_len)

    try:
        sentence += temp_sentence + ' '
        tweet_len -= len(temp_sentence)
    except Exception:
        sentence = model.make_sentence()
    while len(sentence) < 100:
        temp_sentence = model.make_short_sentence(tweet_len)
        if temp_sentence is not None:
            sentence += temp_sentence + ' '
            tweet_len -= len(temp_sentence) + 1

    sentence += "#" + tweeter
    pic_name = tweeter + "_dtm.jpg"
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
    sentence = sentence.encode('utf-8')
    print (sentence)
    try:
        api.update_with_media(path + pic_name, sentence)
    except Exception:
        "you're banned, idiot."


def redetweet(tweeter, user, tid, twit):
    """Retweet a tweet. A good way to get banned."""
    keys = tr.key_access()
    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    api = tweepy.API(auth)

    profile = api.get_user(tweeter)
    pic_add = profile.profile_image_url
    pic = imags.get_twitpic(pic_add.replace("_normal", ""), tweeter)
    pix = pic.load()
    path = "./twits/imgs/{}/".format(tweeter)
    data = tr.twit_reader(tweeter)

    with open("./twits/corpses/" + tweeter + "_corpus.txt", "w") as fp:
        for ii in xrange(len(data)):
            for obj in reversed(data[ii]):
                twit = obj["text"] + "\n"
                fp.write(twit.encode("utf-8"))

    with open("./twits/corpses/" + tweeter + "_corpus.txt", 'r') as cf:
        corpus = cf.read()
        model = markovify.Text(corpus)

    pic_name = tweeter + "test_dtm_0.jpg"
    xx = pic.size[0]
    yy = pic.size[1]

    tweet_len = 120 - len(user)
    sentence = ''
    temp_sentence = model.make_short_sentence(tweet_len)

    while temp_sentence is None:
        temp_sentence = model.make_short_sentence(tweet_len)

    sentence += temp_sentence + ' '
    tweet_len -= len(temp_sentence) + 1

    while len(sentence) < 100:
        temp_sentence = model.make_short_sentence(tweet_len)
        if temp_sentence is not None:
            sentence += temp_sentence + ' '
            tweet_len -= len(temp_sentence) + 1

    sentence += "#" + tweeter

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

    imags.xorror(pix, xx, yy, twit)
    imags.shapes(pix, xx, yy, twit,
                 (ord(twit[66]) / 8) % len(twit) + 1)
    imags.wordler(pic, l1, l2, l3)
    imags.scoots(pix, xx, yy, twit)
    imags.xorror(pix, xx, yy, twit)
    pic.save(path + pic_name)
    sentence = sentence.replace("@", "#")
    sentence = sentence.replace("&amp;", "&")
    # this is what gets you banned
    # sentence = '@' + user + ' ' + sentence

    api.update_with_media(path + pic_name, sentence, in_reply_to_status_id=tid)
