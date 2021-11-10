import requests
from bs4 import BeautifulSoup
import re, urllib, json


def get_character_text(name):

    baseurl = "https://theoffice.fandom.com/api.php?"
    action = "action=query"
    title = f"titles={name}"
    content = "prop=revisions&rvprop=content&rvslots=*"
    dataformat = "format=json"

    query = "{0}{1}&{2}&{3}&{4}".format(baseurl,action,title,content,dataformat)


    with open(f'characters/{name}.txt', 'w') as f:

        response = urllib.request.urlopen(query)
        data = response.read()
        text = data.decode('utf-8')
        content = json.loads(text)
        page_id = list(content['query']['pages'].keys())[0]
        text = content['query']['pages'][page_id]['revisions'][0]['slots']['main']['*']
        f.write(text)

baseurl = "https://theoffice.fandom.com/api.php?"
action = "action=query"
content = "prop=revisions&rvprop=content"
dataformat ="format=json"

# characters are split across two pages
page_titles = ["https://theoffice.fandom.com/wiki/Category:Characters", "https://theoffice.fandom.com/wiki/Category:Characters?from=Merv+Bronte"]
categories = []


for page_title in page_titles:

    title = f"titles={page_title}"
    query = "{}{}&{}&{}&{}&rvslots=*".format(baseurl, action, content, title, dataformat)

    page = requests.get(page_title)

    soup = BeautifulSoup(page.content, "html.parser")
    character_pattern = re.compile(r'/wiki/(.*)')
    category_pattern = re.compile(r'Category:')
    filter_subcategories = ["Background_Employees", "Clients_of_Dunder_Mifflin", "Main_Characters", "Mentioned_characters", "Voiced_Characters", "Background_Warehouse_Employees", "Dunder_Mifflin_family_members_and_loved_ones", "The_Office_Characters", "Angela%27s_cats"]
    # for each of the characters listed in the characters pages
    for link in soup.find_all("a", {"class": "category-page__member-link"}):

        # capture all the href elements
        href = link.get("href")

        # capture all character names in each href
        name =  character_pattern.match(href).group(1)

        # remove "Categories" which are classifications of characters and not characters themselves
        if category_pattern.match(name):
            categories.append(name)

        # remove specific subcategories which are not characters themselves
        elif name not in filter_subcategories:
            get_character_text(name)
