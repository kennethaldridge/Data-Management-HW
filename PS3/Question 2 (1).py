#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import lxml


# In[2]:


#start soup
url = 'https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc'
hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url, headers=hdr)
soup = BeautifulSoup(response.text, 'html.parser')


# In[3]:


#initialize lists
list_titles = []
list_years = []
list_directors = []
list_actors = []
list_ratings = []

for movie in soup.find_all('div', class_ = 'lister-item mode-advanced'):
    #get title and release year
    header = movie.find('h3', class_ = 'lister-item-header')
    title = header.find('a')
    list_titles.append(title.text)
    release_year = header.find('span', class_ = 'lister-item-year text-muted unbold')
    release_year = release_year.text
    #remove () from the year, have to deal with 'Oppenheimer' because have a different year
    if title.text == 'Oppenheimer':
        release_year = release_year.replace('(I) ', '')
        release_year = release_year[1:-1]
        list_years.append(int(release_year))
    else:
        release_year = release_year[1:-1]
        list_years.append(int(release_year))
    
    #get rating
    rating_bar = movie.find('div', class_ = 'ratings-bar')
    rating = rating_bar.find('strong')
    list_ratings.append(float(rating.text))
    
    #get directors and actors
    direct_act_bar = movie.find('p', class_ = "")
    num = 0
    actors = []
    for person in direct_act_bar.find_all('a'):
        if num == 0:
            list_directors.append(person.text)
        else:
            actors.append(person.text)
        num = num + 1
            
    list_actors.append(actors)
    
    


# In[4]:


import pandas as pd

df_movies = pd.DataFrame({'title': list_titles, 'director': list_directors, 
                          'actors': list_actors, 'release_year': list_years, 'rating': list_ratings})

df_movies

