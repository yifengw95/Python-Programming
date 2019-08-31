import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import sys
import requests
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor

# RUN SOURCE 1 REMOTE FIRST!

# sys.argv[1] is the content you typed in the command line
# either 'source1', 'source2' or 'source3'
# sys.argv[2] is second content you typed in the command line
# either 'remote ot' local
if sys.argv[1] == 'source1':
    if sys.argv[2] == 'remote':
        print('\n')
        print('*** Outputing data source 1 *** ')
        print('\n')
        url = 'https://anapioficeandfire.com/api/characters/'
        print('Official JSON API providing information for the Ice and Fire .\n')
        print('we are grabbing the name of each charactor, his gender, his aliases and playedBy. \n')
        print('URL:')
        print(url)
        print('\n')
        print('Sample Output\n')
        df = pd.DataFrame(columns = ['Name','Gender','Aliases','playedBy']) 
        for i in list(range(15,150)):
            tempURL = 'https://anapioficeandfire.com/api/characters/' + str(i)
            response = requests.get(tempURL).json()
            temp = dict()
            temp = {'Name':response['name'],'Gender':response['gender'], 'Aliases':response['aliases'], 'playedBy':response['playedBy']}
            print(temp)
            df = df.append(temp,ignore_index=True)
        df.to_csv('Ice and Fire.csv')
    if sys.argv[2] == 'local':
        myData = pd.read_csv('Ice and Fire.csv')
        print(myData)     


# sys.argv[1] is the content you typed in the command line
# sys.argv[1] is the content you typed in the command line
if sys.argv[1] == 'source2':
    if sys.argv[2] == 'remote':
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
    if sys.argv[2] == 'local':
        myData = pd.read_csv('Ice and Fire.csv')
        print(myData)     

# sys.argv[1] is the content you typed in the command line
if sys.argv[1] == 'source3':
    if sys.argv[2] == 'remote':
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
    if sys.argv[2] == 'local':
        myData = pd.read_csv('Ice and Fire.csv')
        print(myData)     
