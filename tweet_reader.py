"""Read the tweets."""


import json
import os
import zipfile as zf


def twit_reader():
    """Read tweets from a file."""
    twits = []
    path = "./twits/easy_d/"
    pathos = "./twits/trump_tweet_data_archive/"
    zippo = "master_2017.json.zip"

    with zf.ZipFile(pathos + zippo, "r") as zip_rf:
        zip_rf.extractall(path)

    for fn in os.listdir(path):
        with open(fn) as filo:
            data = json.load(filo)
            for obj in reversed(data):
                twits.append(obj["text"])

    return twits
