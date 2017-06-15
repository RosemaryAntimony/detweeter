"""Read the tweets."""

import glob
import json
import os
# from shutil import copyfile
import zipfile as zf


def twit_reader(user):
    """Read tweets from a file."""
    path = "./twits/" + user + '/'

    if user != "realdonaldtrump":
        # pathos = "./twits/" + user + '/'
        zippo = user + "_long*"
    else:
        # pathos = "./twits/" + user + "/"
        zippo = "master_*"

    # if not os.path.exists(path):
    #     os.makedirs(path)

    # for fn in os.listdir(pathos):
    #     try:
    #         copyfile(pathos + fn, path + fn)
    #     except Exception:
    #         print ("Well that one didn't happen.")

    for fn in glob.glob(path + zippo + ".zip"):
        with zf.ZipFile(fn, 'r') as zref:
            zref.extractall(path)

    data = []

    for fn in glob.glob(path + zippo + ".json"):
        with open(fn) as filo:
            data_temp = json.load(filo)
            data.append(data_temp)

    return data


def dezipper(path):
    """Remove jsons."""
    for fn in os.listdir(path):
        os.remove(path + fn)


def key_access():
    """Access twitter API."""
    with open('api_keys.json') as f:
        keys = json.load(f)

    return keys
