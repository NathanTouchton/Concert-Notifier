from os import system

# https://spiritbox.com/pages/tour
# https://architectsofficial.com/tour

def curl(website:str):
    """Runs the curl command for whatever website you pass into it."""
    system(f"curl '{website}'")

print(curl("https://ntprogramming.us"))
