from os import system
# from emailtemplate import SendEmail

# https://spiritbox.com/pages/tour
# https://architectsofficial.com/tour

# Curl websites for HTML
# Determine where to look for city/state names

def curl(website:str):
    """Runs the curl command for whatever website you pass into it."""
    system(f"curl '{website}'")

# curl("https://spiritbox.com/pages/tour")
# Spiritbox html class: bit-location-under-mobile

# curl("https://architectsofficial.com/tour")
# Architects html class: bit-location-under-mobile

# Send email if city and/or state lines up with what I'm looking for
# Prevent from sending too many emails somehow
