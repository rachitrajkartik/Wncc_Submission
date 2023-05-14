#!/usr/bin/env python
# coding: utf-8

# In[64]:


from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://itc.gymkhana.iitb.ac.in/wncc/soc/').content
soup = BeautifulSoup(html_text, 'html.parser')
#print(soup.prettify())
#print(soup.find_all('p'))
#print(soup.title)
#print(soup.get_text())
# all_links = set()
# for link in soup.find_all('a'):
#     linktext = link.get('href')
#     all_links.add(link)
#     print(linktext) 


# In[65]:


project_name = []
project_link = []
project_image = []
names = soup.find_all('p',class_ = "lead text-center font-weight-bold text-dark")
#print(names)
for i in names:
    name = i.text
    project_name.append(name)
# print(len(project_name))
# for i in range(len(project_name)):
#     print(project_name[i])


# In[66]:


for link in soup.find_all('a'):
    if link.get('href') is not None:
        linktext = ("https://itc.gymkhana.iitb.ac.in" + link.get('href'))
        project_link.append(linktext)
# print(len(project_link))
# for i in range(13,len(project_link)):
#     print(project_link[i])


# In[67]:


image_tags = soup.find_all("img")
# Iterate through the image tags and extract the source (src) attribute
for image_tag in image_tags:
    if image_tag.get("src") is not None:
        image_url = ("https://itc.gymkhana.iitb.ac.in" + image_tag.get("src"))
        project_image.append(image_url)
# print(len(project_image))
# for i in range(len(project_image)):
#     print(project_image)


# In[89]:


import numpy as np
import pandas as pd
data = {}

for i in range(1, 72):
    url = project_link[i+11]
    soup2 = BeautifulSoup(requests.get(url).content,'html.parser')
    #print(soup2)
    p_tag = soup2.find_all('ul')
    data[i] = {'Name': project_name[i - 1], 'Link': project_link[i + 11], 'Image': project_image[i+3],'Mentors' : p_tag[3].text,'No. of Mentees' : p_tag[4].text}  

df = pd.DataFrame(data)
df.index.name = 'Index'

df.transpose().to_csv('soc.csv')


# In[ ]:




