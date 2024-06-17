import requests

def main():
    pass
for i in range(100):
    a = "https://pokeapi.co/api/v2/evolution-chain/" + str((i + 1))
    res = requests.get(a)
    if res.status_code == 200:
        dades = res.json()
        print("El nom del pokémon és: {}".format(dades["chain"]["species"]))
        for e in dades["chain"]["evolves_to"]:
            print("Nom de la seva evolució: ", e["species"]["name"])
    else:
        print("No hi ha dades.")

def pokemon (url):
    res=requests.get(url)
    if res.status_code == 200:
        dades = res.json()
        for e in dades["results"]:
            print("url secundaria: "+e["url"])
            pokemon2(e["url"])
    else:
        print("No hi ha més dades.")
def pokemon2 (url):
    res=requests.get(url)
    if res.status_code == 200:
        dades = res.json()
        for e in dades:
            print(e)
    else:
        print("No hi ha més dades.")

# Main Program
a = "https://pokeapi.co/api/v2"
res = requests.get(a)
if res.status_code == 200:
    dades = res.json()
    print(dades)
    for e in dades["pokemon_entries"]:
        pokemon(e["url"])