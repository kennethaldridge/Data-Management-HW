#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
from xml.dom import minidom
import pandas as pd

doc = minidom.parse('recipes.xml')
recipes = doc.getElementsByTagName('recipe')

titles_list = []
recipes_ingredients_list = []
calories_list = []

for recipe in recipes:
    #get the title
    title = recipe.getElementsByTagName('title')[0].firstChild.data
    titles_list.append(title)
    
    #get the list of ingredients
    ingredients_list = []
    for ingredient in recipe.getElementsByTagName('ingredient'):
        ingredient_name = ingredient.getAttribute('name')
        ingredients_list.append(ingredient_name)
    recipes_ingredients_list.append(ingredients_list)
        
    #get the calories
    for nutrition in recipe.getElementsByTagName('nutrition'):
        calories = nutrition.getAttribute('calories')
        calories_list.append(calories)
    
    
df_recipes = pd.DataFrame({'Recipe Name': titles_list, 'Ingredients': recipes_ingredients_list, 'Calories': calories_list})

df_recipes


# In[2]:


#2 XPath
from lxml import etree
tree = etree.parse ('recipes.xml')
#For all queries, not including any sub ingredients, just the main recipes


# In[3]:


#(a) Titles of All Recipes
results_a = tree.xpath('//title')
for result in results_a:
    print(result.text)


# In[4]:


#(b) Find titles of recipes that use olive oil
results_b = tree.xpath('//recipe[ingredient[@name="olive oil"]]/title')
for result in results_b:
    print(result.text)


# In[5]:


#(c) Find title of all recipes with less than 500 calories
results_c = tree.xpath('//recipe[nutrition[@calories<"500"]]/title')
for result in results_c:
    print(result.text)


# In[6]:


#(d) Find amount of sugar needed for Zuppa Ingelese
results_d = tree.xpath('//recipe[title = "Zuppa Inglese"]/ingredient[@name = "sugar"]/@amount')
for result in results_d:
    print(result)


# In[7]:


#(e) Find titles of all recipes that require 4 steps
results_e = tree.xpath('//recipe[count(preparation/step)=4]/title')
for result in results_e:
    print(result.text)


# In[8]:


#(f) Find names of all ingredients that are used to make other ingredients
results_f = tree.xpath('//ingredient[ancestor::ingredient]/@name')
for result in results_f:
    print(result)


# In[9]:


#(g) Find names of all ingredients for which you need other ingredients
results_g = tree.xpath('//ingredient[ingredient]/@name')
for result in results_g:
    print(result)


# In[10]:


#(h) Find the names of the first three ingredients in each recipe
results_h = tree.xpath('//recipe/ingredient[1]/@name|//recipe/ingredient[2]/@name|//recipe/ingredient[3]/@name')
for result in results_h:
    print(result)

