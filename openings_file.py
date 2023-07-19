import requests
from bs4 import BeautifulSoup

response = requests.get("https://lichess.org/opening")
soup = BeautifulSoup(response.content, 'html.parser')
lala = soup.find_all('span', class_='opening__next__name')
opening_names = []
probability = []
move = []
for i in range(len(lala)):
    opening_names.append(str(lala[i]).split(">")[1].split("<")[0])
lala = soup.find_all('span', class_='opening__next__probability')
for i in range(len(lala)):
    probability.append(str(lala[i]).split(">")[1].split("<")[0])
lala = soup.find_all('span', class_='opening__next__san')
for i in range(len(lala)):
    print(lala[i])
    move.append(str(lala[i]).split(">")[1].split("<")[0])
combined = []
for i in range(len(opening_names)):
    combined.append(f"{opening_names[i]}-{probability[i]}-{move[i]}")
print(combined)
