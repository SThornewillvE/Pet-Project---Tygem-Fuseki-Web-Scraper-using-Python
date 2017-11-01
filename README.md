# Tygem Game Scraper

## Description

This script downloads game in search results from the ["Fuseki Info for Tygem Baduk Server" database](tygem.fuseki.info/index.php). This database contains go/baduk game records (216,140) from the "Tygem" Go Server where at least one player is of 8-dan level. To those who are familiar with the game, that is rather strong.

My motivation for writing this script was to review the games of "legend88" who is rumored to be a professional player who was playing against amateurs and is known for his basic and fundamentally sound style. This makes his games very good for review because it shows exactly how amateurs fall short in their games and how to retort to different tricks that might be played against oneself. There are popular streamers such as [Dwyrin](https://www.youtube.com/results?search_query=legend88) who has reviewed many of these games.


The website also has a ["pattern search"](http://tygem.fuseki.info/fuseki.php?f=full&sb=full) feature which allows one to find games based on the moves that were played on the board. This means that it is possible to use the pattern search to find games with commentary and play them out on a real before checking the commentary.

You can find all of the legend88 files here if you are interested.

## How it works

On an operational level, the script works by taking a URL and scraping the games directly from the website. You can find an example URL [here](http://tygem.fuseki.info/games_list.php?sb=full&bs=pl&q=legend88&id=79W892Z0). (Any search result of this format will work)

This is the basic procedure:
* Inputted URL is used to extract the game IDs present on the page
  * There are no direct links to game pages, hence why IDs are scraped
* The page is then searched for the next page in the search, this continues until there is no new page.
* Each ID is concatenated with the relevant URL to doanload the game files
* The game details are scraped from the page and concatenated to make the game name (player names and date)
* If the game name has been used before then the name will be changed to signify a rematch before the file extension is concatenated
* Finally, the game is saved to the hard drive in the same directory as the script
* Please note that time delays were added using "time" in order to not overload the servers.

## How you can use it

This Script is written using Python 3.6 and so you will need to have this version in order to execute the file. You also need all of the dependencies mentioned.

This script is dependtant on the following modules:
* [urllib](https://docs.python.org/3/library/urllib.html)
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [time](https://docs.python.org/2/library/time.html)
* [regular expressions](https://docs.python.org/3/library/re.html)
