import requests
import time
from bs4 import BeautifulSoup


def timer (function): # Decorator Function Example
    def wrapper (rateLimiter):
        start=time.time()
        function(rateLimiter)
        end=time.time()
        print("""
        \t\t**************************
        \t\t{} takes : {} Secs.
        \t\t**************************
        """.format(function.__name__,round(end-start,2)))
    return wrapper

@timer
def Searching (rateLimiter):

    url = "https://www.imdb.com/chart/top/"
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")

    titles = soup.findAll("td", {"class": "titleColumn"})
    rates = soup.findAll("td", {"class": "ratingColumn imdbRating"})

    printCounter = 0 # For Detetecting if there is no search result
    for title, rate in zip(titles, rates):
        title = title.text
        rate = rate.text

        title = title.strip() # replacing unnecessary white spaces
        title = title.replace("\n", "") # replacing unnecessary new lines

        rate = rate.strip() # replacing unnecessary white spaces
        rate = rate.replace("\n", "") # replacing unnecessary new lines


        if float(rate) >= rateLimiter:
            printCounter += 1
            print("Title : ", title, "Rate : ", rate)

    if printCounter == 0: # Controlling if there is no search result
        print("There is no film in the world has this rate point :) ")


while True: # For avoiding miss inputs
    try:
        rateLimiter=float(input("Plase choice the rate : "))
        break
    except ValueError: # If user gives miss matched tipe
        print("Plase use this format X.X ")


Searching(rateLimiter) #Calling the function
