class Player:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def whois(self):
        print (f"{self.name} was born in {self.nationality}")