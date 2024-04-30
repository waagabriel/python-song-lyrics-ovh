import requests
import sys


artista = input("Insira o nome do Artista:\t")
musica  = input("Insira o nome da musica:\t")

Api = "https://api.lyrics.ovh/v1/" + artista + "/" + musica

data = requests.get(Api)

if data.status_code == 404:
    print("Erro ao pesquisar\n")
    sys.exit(1)

letras = str(data.content)
letras = letras.replace('\\n', '\n').replace('\\r', ' ').replace('\\', ' ')
str(letras)


print("\x1b[93m ",letras)
