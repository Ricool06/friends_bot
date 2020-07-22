# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # This notebook is intended to:
# - Ingest the entire collected works of the TV show "Friends"
# - Preprocess the data by extracting text and concatenating into a single document
# - Train a Natural Language Processing model to generate similar works
# - Evaluate the model
# - Save the model so it may be used by a Twitter bot

# %%
from bs4 import BeautifulSoup
import requests
from typing import List
import re


# %%
base_url = 'https://fangj.github.io/friends/'
links = List[str]

with requests.get(base_url) as response:
    html = BeautifulSoup(response.text)
    links = [a['href'] for a in html.find_all('a')]


# %%
def extract_script(path: str) -> str:
    with requests.get(base_url + path) as page_res:
        page_html = BeautifulSoup(page_res.text)
    
    first_scene_annotation = page_html.find(text=re.compile('Scene:'))
     first_scene_annotation.parent.find_next_siblings().parent.find_next_siblings()


# %%
[extract_script(link) for link in links]


# %%



# %%


