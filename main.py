import random


class godspeak():

    def __init__(self, amount: int):
        self.amount = amount
        print(f"ready\namount: {self.amount}")
        self.run()

    def getWords(self):
        with open("./data/vocab.txt", "r") as god:
            self.words = []
            for word in god:
                self.words.append(word.rstrip("\n"))
                #self.words = word[random.randint(0, 10)]
        
        return self.words

    def listify(self):
        with open("./data/vocab.txt", "r") as god:
          for word in god:
            self.words.append(word.rstrip("/n"))

        return self.words
    
    def run(self):
        print(self.getWords())


godspeak(10)