# from os import system
from requests import get
# from emailtemplate import SendEmail

# Curl websites for HTML
# Determine where to look for city/state names

# def curl(website:str):
#     """Runs the curl command for whatever website you pass into it."""
#     return system(f"curl '{website}'")

spiritbox_site = "https://spiritbox.com/pages/tour"
# Spiritbox html class: bit-location-under-mobile

architects_site = "https://architectsofficial.com/tour"
# Architects html class: bit-location-under-mobile

a = get(url=architects_site)
print(a.text)

# Send email if city and/or state lines up with what I'm looking for
# Prevent from sending too many emails somehow
