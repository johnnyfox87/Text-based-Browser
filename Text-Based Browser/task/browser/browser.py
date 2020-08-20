import os
import requests
import sys

from collections import deque

history = deque()
http_str = "https://www."


def print_page(url, text):
    path = directory + "\\" + url[:url.rfind(".")]
    if os.path.exists(path):
        with open(path) as file:
            print(file.read())
    else:
        with open(path, "w") as file:
            file.write(text)
        print(text)


def load_page(url):
    req = http_str + url
    r = requests.get(req)
    if r:
        history.append(url)
        print_page(url, r.text)
    else:
        print("error: address not found: ", url)


# Read args
args = sys.argv
if len(args) == 2:
    directory = args[1]
    if not os.path.isdir(directory):
        os.mkdir(directory)
else:
    print("error: no directory given")
    sys.exit()

# Look for website
input_text = ""
while True:
    input_text = input("URL:")
    if input_text == "exit":
        break
    input_text.replace(http_str, "")
    if input_text == "back":
        if len(history) > 1:
            history.pop()
            print_page(history[len(history) - 1])
    elif input_text.find(".") < 0:
        print("error: invalid address")
    else:
        load_page(input_text)
