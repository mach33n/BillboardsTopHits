from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.billboard.com/charts/rap-song'

# opening up connection to billboard page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each container in top 25
containers = page_soup.findAll("div",{"class":"chart-row__title"})

print("Top Hip-Hop Songs")

for container in containers:

    songTitle = container.h2.text
    songArtist = container.a.text

    print(containers.index(container) + 1)
    print("Song Title:" + songTitle)
    print("Song Artist:" + songArtist)
