import requests

query = input("What news do you want to read today: ")

api = "6b3e51204899499b870fdcaeee385673"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-12-16&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for i, article in enumerate(articles):
    print(i+1, f"Title: {article["title"]}","\n",f"URL:", article["url"])
    print("\n*********************************************\n")