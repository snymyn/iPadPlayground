import requests, bs4

"""
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
type(res)

res.status_code == requests.codes.ok

len(res.text)

play_file = open("RomeoAndJuliet.txt", "wb")
for chunk in res.iter_content(100000):
	play_file.write(chunk)

"""

"""
res = requests.get("http://nostarch.com")
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text)
type(no_starch_soup)

"""

res = requests.get("http://google.com")
res.raise_for_status()

