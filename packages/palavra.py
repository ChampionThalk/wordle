import requests

class Palavra:
    def random_word():

        palavra = requests.get("http://papalavras-server.herokuapp.com/words/random/")


        return palavra
    


c = requests.get("http://papalavras-server.herokuapp.com/words/random/")

print(c)