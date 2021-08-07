import sys
from typing import Tuple
from hashlib import md5, sha1
from os import walk, path


def sync_local_image(dir_name) -> Tuple:
    image_file_ext = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    return (
        path.join(dp, f)
        for dp, dn, filenames in walk(dir_name)
        for f in filenames
        if path.splitext(f)[1] in image_file_ext
    )


def get_hash(file_name) -> Tuple:
    BUF_SIZE = 65536  # ground to 65535
    with open(file_name, "rb") as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
    return (md5.hexdigest(), sha1.hexdigest())
