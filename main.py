import requests

query = input("what type of news are you interested in today? ")
api = "7d301898e9e047c1b6005d6f93dfa970"
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-06-14&to=2026-06-14&sortBy=popularity&apiKey={api}"


print(url)
r= requests.get(url)

data = r.json() # JSON = a format for sharing data on the internet 

print(data)
articles = data["articles"]

for index, article in enumerate(articles):
    # dictinary indexing
    print(f"{index+1}. {article["title"]}") 
    print(f"URL: {article["url"]}")
    print("\n*****************************\n")  