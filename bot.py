import requests
from bs4 import BeautifulSoup
import time
import re
import html
import urllib

url = 'https://www.urban-living-nuernberg.de/mieten'

page = requests.get(url)

if(page.status_code == 200):

    webSoup = BeautifulSoup(page.text, 'html.parser')
    apartment_list = webSoup.find(id="apartmentanlage").find_all("a", attrs={"class":"apartment","class":"d-none"})

    for apartment in apartment_list:

        apartmentSoup = BeautifulSoup(apartment.get("data-text"), 'html.parser')
        apartmentTitleSoup = BeautifulSoup(apartment.get("title"), 'html.parser')
        apartmentImageSoup = BeautifulSoup(apartment.get("data-img"), 'html.parser')

        occupation = apartmentSoup.span['class']

        if(occupation[0] != 'unit_occupied' and occupation[0] != 'unit_reserved'):
            apartment = str(apartmentSoup).split("<br/>")
            apartmentImage = "https://www.urban-living-nuernberg.de" + str(apartmentImageSoup)
            apartmentTitle = str(apartmentTitleSoup)
            request = requests.get("https://api.telegram.org/bot<bottoken>/sendMessage?chat_id=<chatid>&text=" + urllib.parse.quote_plus("APARTMENT FREI\n" + apartmentImage + "\nStockwerk:\n" + apartment[0] + "\n\nBalkon:\n"+ apartment[1] + "\n\nAusrichtung:\n" + apartment[2] + "\n\n" + apartment[6] + "\n" + apartment[7] + "\n\n" + apartmentTitle + "\n" + url))
