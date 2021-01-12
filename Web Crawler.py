# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0602

Scott Elmore
10/29/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://youtu.be/WKmA3GEOByA
"""

from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser
import re


class Collector(HTMLParser):
    'collects hyperlink URLs into a list; and contents of data into a list'

    def __init__(self, url):
        'initializes parser, the url, a list of links, a list of data and a list of start tags'
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        self.data = []
        self.st_tags = []

    def handle_starttag(self, tag, attrs):
        'collects hyperlink URLs in their absolute format; adds starts tags to a list'
        self.st_tags.append(tag)

        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # construct absolute URL
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':  # collect HTTP URLs
                        self.links.append(absolute)

    def handle_data(self, data):
        '''handle data by stripping it of white space and adding it to list of tuples;
        tuple also contains start tag'''

        stp_data = data.strip()
        # make sure there is a previous start tag
        if len(self.st_tags) > 0:
            if stp_data:
                # add data along with start tag, to be used in
                # determining what qualifies as a word on a page
                self.data.append((self.st_tags[-1], stp_data))

    def getLinks(self):
        'returns hyperlinks URLs in their absolute format'
        return self.links

    def getData(self):
        'returns data in a (starttag, data_content) format'
        return self.data

# initalize base_url variable to make sure links are within scope of this url
base_url = 'https://www.cdm.depaul.edu/'

# initialize string of url suffix that duplicates the current page
dup_page = '#ctl00_pagebody'

#this link suffix was causing program to run for > 1 hour
#course_eval = 'course-evaluation' 

download = 'download' 

def webCrawl(url, visited=None, word_dict=None):
    '''a recursive web crawler that calls analyze()
       on every visited web page; pass in a url, set of visited lists, 
       and the word dictionary for keeping track of counted words'''


    # how to pass immutable data structures into a recursive function
    # initializes them is they are set to None
    if visited is None:
        visited = set()
    if word_dict is None:
        word_dict = {}

    # keep track of already visited urls
    visited.add(url)

    # analyze() returns a list of hyperlink URLs in web page url
    links, word_dict = analyze(url, word_dict)

    # recursively continue crawl from every link in links
    for link in links:
        # follow link only if not visited, within url scope, not a duplicate page
        # not a course eval page, and doesn't contain a space character
        if link not in visited and link[:27] == base_url and ' ' not in link \
        and dup_page not in link and download not in link:
            try:
                # recursively call this function, passing in visited url list and word dictionary
                webCrawl(link, visited, word_dict)
            except:
                pass

    # return word dictionary to caller
    return word_dict


def frequency(data_tup_list, word_dict):
    '''function for counting the frequency of each word ona webpage'''
    for data_tup in data_tup_list:
        # if start tag == 'scipt', the data contained is not that of webpage text
        if data_tup[0] != 'script':

            # data contains combination of words that need to be split
            for word_messy in data_tup[1].split():
                # indiviual words needs to be stripped of all miscellaneuous characters and
                #put in lowercase
                word_clean = re.findall(
                    "[a-zA-Z]+", word_messy.strip().lower())
                for word in word_clean:
                    # make sure word is > 1 character
                    if len(word) > 1:
                        # increment word count if in word_dict
                        if word in word_dict:
                            word_dict[word] += 1
                        else:
                            word_dict[word] = 1
    return word_dict


def analyze(url, word_dict):
    '''function for getting urls and data contained on a webpage'''

    print('\n\nVisiting', url)           # for testing

    # obtain links in the web page
    content = urlopen(url).read().decode().lower()

    # initalize Collector class with url, feed in content of page
    collector = Collector(url)
    collector.feed(content)

    # get back the urls into a list
    urls = collector.getLinks()

    # get data in a list of (start_tag, data) tuples
    data_tup_list = collector.getData()

    # calculate frequency of words on page and return a word dictionary
    word_dict = frequency(data_tup_list, word_dict)

    # helper code for printing top 10 words as they exist in the current dicitonary
#    helper = sorted(word_dict.items(), key = lambda x: x[1], reverse=True)
#    print('\nTop 10' )
#    for top in helper[:10]:
#        print(top)

    # return the url list and the word dictionary
    return urls, word_dict


# set first url
url = 'https://www.cdm.depaul.edu/'

# call webCrawl and return the word dictionary
word_dict = webCrawl(url)

# print top 25 words in word dictionary
top = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
print('\nTop 25 words on CDM website\n')
print('{:20}   {:>20}'.format('WORD', 'COUNT'))
print('-'*43)
for word in top[:25]:
    print('{:20} : {:20}'.format(word[0], word[1]))
