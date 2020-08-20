import sys
import os
from collections import deque

history = deque()

pages = {
    "nytimes.com": '''
    This New Liquid Is Magnetic, and Mesmerizing
    
    Scientists have created “soft” magnets that can flow 
    and change shape, and that could be a boon to medicine 
    and robotics. (Source: New York Times)
    
    
    Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.
    
    Jessica Wade has added nearly 700 Wikipedia biographies for
     important female and minority scientists in less than two 
     years.
    
    ''',

    "bloomberg.com": '''
    The Space Race: From Apollo 11 to Elon Musk
    
    It's 50 years since the world was gripped by historic images
     of Apollo 11, and Neil Armstrong -- the first man to walk 
     on the moon. It was the height of the Cold War, and the charts
     were filled with David Bowie's Space Oddity, and Creedence's 
     Bad Moon Rising. The world is a very different place than 
     it was 5 decades ago. But how has the space race changed since
     the summer of '69? (Source: Bloomberg)
    
    
    Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters
    
    Twitter and Square Chief Executive Officer Jack Dorsey 
     addressed Apple Inc. employees at the iPhone maker’s headquarters
     Tuesday, a signal of the strong ties between the Silicon Valley giants.
    '''
}


def print_page(url):
    path = directory + "\\" + url[:url.rfind(".")]
    if os.path.exists(path):
        with open(path) as file:
            print(file.read())
    else:
        with open(path, "w") as file:
            file.write(pages[url])
        print(pages[url])


def find_page(url):
    if url in pages:
        history.append(url)
        print_page(url)
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
text = ""
while True:
    text = input("URL:")
    if text == "exit":
        break
    text.replace("https://www.", "")
    if text == "back":
        if len(history) > 1:
            history.pop()p
            print_page(history[len(history) - 1])
    elif text.find(".") < 0:
        print("error: invalid address")
    else:
        find_page(text)
