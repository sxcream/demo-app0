import requests

r = requests.get('http://www.exemple.com')
print(r.status_code)

a = "hello world !"
print(a)


#affiche le contenu du fichier extension.txt 
with open("extension.txt", "r") as f:
    contenu = f.read()
print(contenu)