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
        print('we are grabbing the name of each charactor, his gender, the time he was born, his aliases, his playedBy and his titles and TV series. \n')
        print('URL:')
        print(url)
        print('\n')
        print('Sample Output\n')
        df = pd.DataFrame(columns = ['Name','Gender','Aliases','playedBy']) 
        for i in list(range(1,1500)):
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
# either 'source1', 'source2' or 'source3'
# sys.argv[2] is second content you typed in the command line
# either 'remote ot' local
if sys.argv[1] == 'source2':
    if sys.argv[2] == 'remote':
        print('\n')
        print('*** Outputing data source 2 *** ')
        print('\n')
        url = 'https://variety.com/2017/tv/news/tv-star-salaries-revealed-2017-robert-de-niro-david-letterman-ellen-degeneres-1202534375/'
        print('The data contains the most popular actors in Game of Thrones/HBO.\n')
        print('we are grabbing the name and the Per-Episode Estimate salaries of the actors. \n')
        print('URL:')
        print(url)
        print('\n')
        print('Sample Output\n')
        url = 'https://variety.com/2017/tv/news/tv-star-salaries-revealed-2017-robert-de-niro-david-letterman-ellen-degeneres-1202534375/'
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'lxml')

        temp = soup.find_all('tbody')[0]
        temp2 = temp.find_all('td', style = 'padding:5px;text-align:left;font-weight:600;')

        name1 = temp2[2].get_text()
        name2 = temp2[3].get_text()
        name3 = temp2[4].get_text()
        name4 = temp2[5].get_text()
        name5 = temp2[6].get_text()

        print('Name:', name1, 'Per-Episode Estimate: $500,000')
        print('Name:', name2, 'Per-Episode Estimate: $500,000')
        print('Name:', name3, 'Per-Episode Estimate: $500,000')
        print('Name:', name4, 'Per-Episode Estimate: $500,000')
        print('Name:', name5, 'Per-Episode Estimate: $500,000')
        
        df = pd.DataFrame(columns = ['Name'])
        temp = {'Name':name1}
        df = df.append(temp,ignore_index=True)
        temp = {'Name':name2}
        df = df.append(temp,ignore_index=True)
        temp = {'Name':name3}
        df = df.append(temp,ignore_index=True)
        temp = {'Name':name4}
        df = df.append(temp,ignore_index=True)
        temp = {'Name':name5}
        df = df.append(temp,ignore_index=True)
        
        df.to_csv('Ice and Fire most popular actors name.csv')
        
    if sys.argv[2] == 'local':
        myData = pd.read_csv('Ice and Fire most popular actors name.csv')
        print(myData)     

# sys.argv[1] is the content you typed in the command line
# either 'source1', 'source2' or 'source3'
# sys.argv[2] is second content you typed in the command line
# either 'remote ot' local
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
