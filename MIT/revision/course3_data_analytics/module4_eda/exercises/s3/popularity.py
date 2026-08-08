from ucimlrepo import fetch_ucirepo

online_news_popularity = fetch_ucirepo(id=332)
X = online_news_popularity.data.features
y = online_news_popularity.data.targets

# metadata
print(online_news_popularity.metadata)

# variable information
print(online_news_popularity.variables)
