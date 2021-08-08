# -*- coding: utf-8 -*-
import time
import urllib.request
from urllib.parse import quote
import string
import re
import json
import os.path


def download_cover(music_name):

    # if cover exsit, will use local cache
    if os.path.isfile("./cover/"+music_name+".png"):
        return 1
    else:
        time.sleep(1) # @todo

    url = "https://maimai.fandom.com/zh/wiki/" + music_name
    s = quote(url, safe=string.printable)
    response = urllib.request.urlopen(s)
    content = response.read().decode("utf-8")
    pattern = re.compile(
        '<div class="floatnone">(.*?)</div>',
        re.S)
    items = re.findall(pattern, content)

    if len(items) < 1:
        return -1
    content = items[0]
    pattern = re.compile(
        '<a href="(.*?)" class="image">',
        re.S)
    items = re.findall(pattern, content)
    if len(items) < 1:
        return -2

    # replace &amp; -> &
    img_url = items[0]
    img_url = img_url.replace("&amp;","&")
    img_url = img_url.replace(" ", "_")

    response = urllib.request.urlopen(img_url)
    with open("./cover/"+music_name+".png", "wb") as f:
        f.write(response.read())

    return 0
