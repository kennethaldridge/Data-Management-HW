#!/usr/bin/env python
# coding: utf-8

# In[12]:


import json
import requests
from pandas.io.json import json_normalize
import pandas as pd


# In[15]:


def get_directions():
    query = 'https://www.mapquestapi.com/directions/v2/route'

    origin = input('Enter an origin: ')
    destination = input('Enter a destination: ')
    params = {'key':'tPpUnj8GBDBMGubfUgzwjuKtcKyC5gGO', 'from': origin, 'to': destination}

    r = requests.get(query, params)
    directions = json.loads(r.text)

    narratives = []
    distances = []
    times = []

    route = directions['route']
    legs = route['legs']

    for leg in legs:
        maneuvers = leg['maneuvers']
        for maneuver in maneuvers:
            narratives.append(maneuver['narrative'])
            distances.append(maneuver['distance'])
            times.append(maneuver['time'])
         
    df_directions = pd.DataFrame({'instruction': narratives, 'distance': distances, 'time (s)': times})
    
    return df_directions


# In[16]:


get_directions()

