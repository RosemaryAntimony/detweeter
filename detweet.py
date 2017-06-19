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
    path = "./twits/imgs/{}/".format(tweeter)

    data = tr.twit_reader(tweeter)

    with open("./twits/corpses/{}_corpus.txt".format(tweeter), "w") as fp:
        for ii in xrange(len(data) if len(data) < 5000 else 5000):
            for obj in data[ii]:
                twit = "{}\n".format(obj["text"])
                fp.write(twit.encode("utf-8"))

    with open("./twits/corpses/{}_corpus.txt".format(tweeter), 'r') as cf:
        corpus = cf.read()
        model = markovify.Text(corpus, state_size=2)

    tweet_len = 138 - len(tweeter)
    sentence = ''
    temp_sentence = model.make_short_sentence(tweet_len)

    try:
        sentence += '{} '.format(temp_sentence)
        tweet_len -= len(temp_sentence)
    except Exception:
        sentence = model.make_sentence()
    while len(sentence) < 100:
        temp_sentence = model.make_short_sentence(tweet_len)
        if temp_sentence is not None:
            sentence += temp_sentence + ' '
            tweet_len -= len(temp_sentence) + 1

    sentence += "#{}".format(tweeter)
    pic_name = "{}_dtm.jpg".format(tweeter)
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
