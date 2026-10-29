import urllib.request
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv"
urllib.request.urlretrieve(url, "data/online_shoppers_intention.csv")