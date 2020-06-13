#!/usr/bin/env python3

import re
import os

DIR = "cran/cran.all.1400"
data = ""

with open(DIR) as fd:
    data = fd.read()

data.strip()
matches = re.compile("\.I [0-9]+").split(data)

matches = list(map(lambda x: x.strip(), matches))

for i in range(len(matches)):
    try:
        split = matches[i].split(".W\n")
        body = split[1]
        metadata = split[0]
        metadata = re.compile("\.[TAB]\n").split(metadata)
        metadata = ''.join(metadata[1:])
        os.system("mkdir cran_new/" + str(i))
        with open("cran_new/" + str(i) + "/body.txt", "w") as fd:
            fd.write(body)
        with open("cran_new/" + str(i) + "/metadata.txt", "w") as fd:
            fd.write(metadata)
    except IndexError as ie:
        pass