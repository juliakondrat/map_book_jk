import requests
from pyexpat import features

from bs4 import BeautifulSoup
import folium

users: list= [
    {'name': 'Julia', 'location': 'Ząbki','posts':10,'picture':'https://www.wig.wat.edu.pl/index.php/component/joomgallery/image?view=image&format=raw&type=orig&id=1443'},
    {'name': 'Julia', 'location': 'Sokółka','posts':20,'picture':'https://www.wig.wat.edu.pl/index.php/component/joomgallery/image?view=image&format=raw&type=orig&id=1443'},
    {'name': 'Klaudia', 'location': 'Warszawa','posts':15,'picture':'https://www.wig.wat.edu.pl/index.php/component/joomgallery/image?view=image&format=raw&type=orig&id=1443'},
    {'name': 'Marcin', 'location': 'Grudziądz','posts':1000,'picture':'https://www.wig.wat.edu.pl/index.php/component/joomgallery/image?view=image&format=raw&type=orig&id=1443'},
    {'name': 'Mateusz', 'location': 'Lublin','posts':100,'picture':'https://www.wig.wat.edu.pl/index.php/component/joomgallery/image?view=image&format=raw&type=orig&id=1443'},
]

def get_coordinates(location_name: str) -> list:
    adres_url = f'https://pl.wikipedia.org/wiki/{location_name}'
    response = requests.get(adres_url)
    response_html = BeautifulSoup(response.text, 'html.parser')


    return [
        float(response_html.select('.latitude')[1].text.replace(',', '.')),
        float(response_html.select('.longitude')[1].text.replace(',', '.'))
    ]

coordinate = get_coordinates('Warszawa')
print(coordinate)

mapa= folium.Map(location=coordinate, zoom_start=6, tiles = 'OpenStreetMap')
for users in users :
    folium.Marker(
    location= get_coordinates(users['location']),
    popup= f'<h3><strong> {users["location"]}</strong></h3><br/> {users["name"]} ({users["posts"]})'
           f'<img  src={users["picture"]} alt="Girl i na jacket" width = "500" height="600">)',
    ).add_to(mapa)
mapa.save('moja mapa.html')




