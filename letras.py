import requests
import sys

artista = input("\x1b[31mInsira o nome do Artista:\t")
musica  = input("\x1b[38;5;18mInsira o nome da musica:\t")

Api = f"https://api.lyrics.ovh/v1/{artista}/{musica}"

data = requests.get(Api)

if data.status_code == 404:
    print("\x1b[38;5;52mErro ao pesquisar\n")
    sys.exit(1)

letras = str(data.content)
letras = letras.replace('\\n', '\n').replace('\\r', ' ').replace('\\', ' ')


print("\x1b[93m ",letras)
