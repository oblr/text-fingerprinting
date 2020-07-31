

import hashlib

def md5_content(text):
    hash_md5 = hashlib.md5(text.encode())
    return hash_md5.hexdigest()


def md5(fname):
    with open(fname, "r") as f:
        h = md5_content(f.read())
    return h


def md5_file(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:

        # h = md5_content(f.read())
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


