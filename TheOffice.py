import requests
from bs4 import BeautifulSoup

baseurl = "https://theoffice.fandom.com/api.php?"
action = "action=query"
content = "prop=revisions&rvprop=content"
dataformat ="format=json"

page_titles = ["Main_Characters"]

#"Former_Employees", "Warehouse_worker"

for page_title in page_titles:

    title = f"titles={page_title}"
    query = "{}{}&{}&{}&{}&rvslots=*".format(baseurl, action, content, title, dataformat)

    response = requests.get(query)

    soup = BeautifulSoup(response.content, "html.parser")

    html_reponse = eval(str(soup))

    page_id = list(html_reponse["query"]["pages"].keys())[0]
    raw_text = html_reponse["query"]["pages"][page_id]["revisions"][0]['slots']['main']['*']
    print(raw_text)

    # with open(f'../files/zelda_characters/{character}.txt', 'w') as f:
    #     json.dump(json_text, f)
