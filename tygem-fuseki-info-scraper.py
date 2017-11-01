#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:18:22 2017

@author: simon
"""

# =============================================================================
# Import libraries
# =============================================================================

import urllib.request
from bs4 import BeautifulSoup
import time
import re


# =============================================================================
# Define Functions
# =============================================================================

def get_ids(soup):
    """
    Checks soup for game IDs and returns it as a list
    """ 
    # Initialize list
    game_ids = []
    
    # Find Game IDs
    for line in soup.findAll('tr'):
        if "OpenGame" in str(line) and re.match('^[a-zA-Z0-9_]+$',str(line)[31-8:31]): 
            game_ids.append(str(line)[31-8:31])
    
    return game_ids


def get_urls(soup):
    """
    Checks page any any links in case there are many games
    Returns list of possible URLs
    """
    # Initialize list
    up_next = []
    
    # Find candidate hyperlinks
    for link in soup.find_all('a'):
        if len(link.get('href')) > 34: up_next.append(link.get('href'))
    
    return unique_lists(up_next)


def unique_lists(listVar):
    """
    Checks list to make sure each value is unique
    """
    # Initialize list
    uniques = []
    
    # Check list
    for item in listVar:
        if not item in uniques: uniques.append(item)
        
    return uniques


def get_game_name(game_id):
    """
    Uses game ID to load the game file and find match details, it then synthesises
    the details into a game name which is returned
    """
    # Initialze base URL
    game_url = 'http://tygem.fuseki.info/game.php?id='+game_id
    
    # Scrape Page
    sauce = urllib.request.urlopen(game_url).read()
    soup = BeautifulSoup(sauce, 'lxml')
    soup_string = str(soup).split('\n')
    
    # Analyze Page
    for line in soup_string:
        if 'Black rank' in line: detail_line = line
        if 'Date' in line: date_line = line

    # Don't overload host
    time.sleep(2)
    
    # Cut things down in a way that will make anyone cry
    # I'm so sorry
    detail_line = detail_line[31:800-16].split('<\\/a><br>')
    black_name = detail_line[0].split('>')[-1].split('(')[0].strip()
    white_name = detail_line[2].split('>')[-1].split('(')[0]
    date_occured = detail_line[-2].split('q=')[-1].split('>')[-1]
    
    # Stitch name together
    game_name = black_name + "-" + white_name + "-" + date_occured

    return game_name




# =============================================================================
# Scrape Page
# =============================================================================
    
"""
url I am working with:
http://tygem.fuseki.info/games_list.php?sb=full&bs=pl&q=legend88&id=79W892Z0
"""

#input URL
url = input("Please enter URL to scrape http://from tygem.fuseki.info \n\n >>>")

# Initialize game ID and history lists
print("Init...")
game_ids = []
history = [url]

# Crawl Pages
print("Begin crawling pages")
flag = True
while flag:
    # Parse Page
    print("Scraping from:", url)
    sauce = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sauce, 'lxml')
    
    # Get i.d. codes for each game
    game_ids+= get_ids(soup)
    
    # Check for "next", follow that link and do the same thing
    up_next = get_urls(soup)[0]
    
    if up_next not in history:
        url = up_next
        print("next:", url)
    else: flag=False
        
    # Don't overload host
    time.sleep(2)
        
# Use ids in game_ids to pull game files
save_url_part = 'http://tygem.fuseki.info/save_game.php?id='
name_history = []
for i in game_ids:
    print("Getting details for:", i)
    # initialize value
    copies = "-rematch"
    
    # Splice save url
    save_url= save_url_part + i
    
    # Get game name
    game_name= get_game_name(i).replace(" ", "")
    
    # Check game name is unique
    if game_name in name_history:
        while game_name in name_history:
            game_name = game_name+copies
    name_history.append(game_name)
    game_name = game_name+".sgf"
          
    # Save file
    urllib.request.urlretrieve(save_url, game_name)
    print(game_name, "saved! \n")