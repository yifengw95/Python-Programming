
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import sys
import requests

	# sys.argv[1] is the content you typed in the command line
	# sys.argv[1] is the content you typed in the command line
if sys.argv[1] == 'source1':
    print('\n')
    print('*** Outputing data source 1 *** ')
    print('\n')
    url = 'http://api.cfl.ca/v1/games/2015?key=T8Mv9BRDdcB7bMQUsQvHqtCGPewH5y8p'
    print('Official JSON API providing real-time league, team and player statistics about the CFL .\n')
    print('we are grabbing the game id and the date to start. \n')
    print('URL:')
    print(url)
    print('\n')
    print('Sample Output\n')
    url = 'http://api.cfl.ca/v1/games/2015?key=T8Mv9BRDdcB7bMQUsQvHqtCGPewH5y8p'
    response = requests.get(url).json()
    games = response['data']
    for game in games[0:3]:
        game_id = game['game_id']
        date_start = game['date_start']
        print(game_id)
        print(date_start)


# sys.argv[1] is the content you typed in the command line
if sys.argv[1] == 'source2':
    print('\n')
    print('*** Outputing data source 2 *** ')
    print('\n')
    url = 'https://book.douban.com/'
    print('The data contains the most popular books nowadays in the China largest reading website.\n')
    print('we are grabbing the name and the detail description link of the book. \n')
    print('URL:')
    print(url)
    print('\n')
    print('Sample Output\n')
    url = 'https://book.douban.com/'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')

    temp2 = soup.find_all('div', class_="title")

    name1 = temp2[1].get_text()
    name1 = name1[1:len(name1)-1]
    link1 = temp2[1].find('a').get('href', None)
    print(name1, link1)

    name1 = temp2[2].get_text()
    name1 = name1[2:len(name1)-1]
    link1 = temp2[2].find('a').get('href', None)
    print(name1, link1)

    name1 = temp2[3].get_text()
    name1 = name1[3:len(name1)-1]
    link1 = temp2[2].find('a').get('href', None)
    print(name1, link1)

# sys.argv[1] is the content you typed in the command line
if sys.argv[1] == 'source3':
    print('\n')
    print('*** Outputing data source 3 *** ')
    print('\n')
    url = 'https://www.imdb.com/movies-in-theaters/?ref_=nv_tp_inth_1'
    print('It contains the movie imformation.\n')
    print('we are grabbing the Movie Synopsis. \n')
    print('URL:')
    print(url)
    print('\n')
    print('Sample Output\n')
    url = 'https://www.imdb.com/movies-in-theaters/?ref_=nv_tp_inth_1'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    temp2 = soup.find_all('td', class_="overview-top")

    print(temp2[0].find_all('div', class_ = 'outline')[0].get_text()[3:])
    print(temp2[1].find_all('div', class_ = 'outline')[0].get_text()[3:])
    print(temp2[2].find_all('div', class_ = 'outline')[0].get_text()[3:])

