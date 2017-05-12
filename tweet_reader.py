"""Read the tweets."""


import glob
import json
import os
import zipfile as zf


def twit_reader():
    """Read tweets from a file."""
    twits = []
    path = "./twits/easy_d/"
    pathos = "./twits/trump_tweet_data_archive/"
    # zippo = "master_2017.json.zip"

    for fn in glob.glob(pathos + "master_*"):
        with zf.ZipFile(fn, "r") as zip_rf:
            zip_rf.extractall(path)

    for fn in os.listdir(path):
        with open(path + fn) as filo:
            data = json.load(filo)
            for obj in reversed(data):
                twits.append(obj["text"])

    dezipper(path)
    return twits


def dezipper(path):
    """Remove jsons."""
    for fn in os.listdir(path):
        os.remove(path + fn)
