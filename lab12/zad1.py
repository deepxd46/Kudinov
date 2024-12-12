import sys
import hashlib
import difflib

cached_sum = ""

def sha256sum(filename):
    with open(filename, 'rb', buffering=0) as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def decode():
    global cached_sum

    sha256 = sha256sum("D:\\GITHUB\\Kudinov\\lab12\\file.txt")
    print(sha256)

    cached_sum = sha256

    with open("D:\\GITHUB\\Kudinov\\lab12\\file.txt", "a") as f:
        f.write(sha256)

    return

def encode():

    with open("D:\\GITHUB\\Kudinov\\lab12\\file.txt", "r") as f:
        original_data = f.read()[:-64]

    with open("D:\\GITHUB\\Kudinov\\lab12\\file.txt", "w") as f:
        f.write(original_data)

    newSha256 = sha256sum("D:\\GITHUB\\Kudinov\\lab12\\file.txt")

    print(newSha256)

    print(str(cached_sum) == str(newSha256))
    
    return

decode()
encode()