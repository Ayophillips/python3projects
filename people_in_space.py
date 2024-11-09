#Run 'pip install requests' to use request mode
import requests

people = requests.get('http://api.open-notify.org/astros.json')
data = people.json()

print(data)

print("The people currently in space are:")
for person in data["people"]:
    print(person["name"])