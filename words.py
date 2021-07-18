""" Retrive and print words from URL

Usage:

    python words.py <URL>
"""

import sys
from urllib.request import urlopen

# Function to fetch words and example of docstrings position


def fetch_words(url):
    """Fetch a list of words from URL. 

Args:
    url - The URL of a UTF-8 document. 

Returns:
    A list of strings containing the words from the document.

"""
    story = urlopen(url)  # 'http://sixty-north.com/c/t.txt'
    story_words = []

    for line in story:
        # Decodeing bytes transfered over HTTP
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """ Print items one per line 

    Args:
        An iterable series of printable items
    """
    # Bytes transfered over HTTP not strings
    for item in items:
        print(item)


def main(url):  # Argument to be avaliable to main function url argument
    """Print each word from a text document from at a URL

    Args:
        url: The URL of a UTF-8 text document
    """
    # url = sys.argv[1] #From sys module to except inputs from command line, but need to go in main func arg
    words = fetch_words(url)
    print_items(words)


# If dunder name is eqal to dunder main it executes the function as script!
# If it is not then it just load function (import to other module)
# and does not execute it.
if __name__ == '__main__':
    # Added from main function in to the global environment of module
    main(sys.argv[1]) #The 0 argument is the module filename!!!
