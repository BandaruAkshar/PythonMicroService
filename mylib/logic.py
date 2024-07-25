import wikipedia
from textblob import TextBlob

def wiki(name="War Goddess", length=1):
    """This is a Wikipedia fetcher"""
    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search_wiki(name):
    """Search wikipedia for names"""
    results = wikipedia.search(name)
    return results

def phrase(name):
    """Returns Phrases from Wikipedia"""
    page = wiki(name)
    blob = TextBlob(page)
    phrases = blob.noun_phrases
    return phrases