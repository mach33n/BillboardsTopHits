from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.youtube.com/results?search_query=abridged'

# opening up connection to billboard page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each container in top 25
containers = page_soup.findAll("div",{"class":"yt-lockup-content"})

print(len(containers))

print("Abridged Episode List: ")

for container in containers:
    if container is not None:
            print(container.a.text)
