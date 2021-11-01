import urllib.request


def obtain_webpage(url: str):
    return urllib.request.urlopen(url)

