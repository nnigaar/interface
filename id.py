import requests
wiki_api_url = "https://tr.wikipedia.org/w/api.php"
page_title = "Albert Einstein"

params = {
    "action": "query",
    "format": "json",
    "titles": page_title,
    "prop": "info",
    "inprop": "url"
}
response = requests.get(url=wiki_api_url, params=params)
data = response.json()
page_id = list(data["query"]["pages"].keys())[0]
print("Page ID for", page_title, ":", page_id)

