#!/usr/bin/env python3

import os
from pathlib import Path
from json import load


DATAFILE_NAME = "mime_data.json"
STATIC_DIR = "./"


if __name__ == "__main__":
    with open(DATAFILE_NAME, 'r') as f:
        d = load(f)
    for item in d:
        mime_head, mime_tail = item["mime"].split("/")
        ext = item["ext"]
        Path(STATIC_DIR + mime_head + "/").mkdir(exist_ok=True)
        with open(STATIC_DIR + mime_head + "/" + mime_tail, 'w') as f:
            f.write(ext)