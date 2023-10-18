from requests import get
from bs4 import BeautifulSoup
# from emailtemplate import SendEmail

# Scrape websites for HTML
# Determine where to look for city/state names

spiritbox_site = "https://spiritbox.com/pages/tour"
# Spiritbox html class: bit-location-under-mobile

architects_site = "https://architectsofficial.com/tour"
# Architects html class: bit-location-under-mobile

architects = get(url=architects_site).text
soup = BeautifulSoup(architects, "html.parser")
# print(soup.find("a", {"class": "bit-details"}))
print(soup.prettify())

# Send email if city and/or state lines up with what I'm looking for
# Prevent from sending too many emails somehow

# It looks like I'll need to use Selenium
