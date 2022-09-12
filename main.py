import random
import json


class godspeak():

    def __init__(self, amount: int):
        self.amount = amount
        print(f"ready\namount: {self.amount}")
        self.run()

    def getWords(self):
        with open("./data/vocabList.json", "r") as god:
            data = json.load(god)
            #print(data)
            self.words = []
            count = 0
            cont = True
            while cont is True:
                if count < self.amount:
                    self.words.append(data[random.randint(0, 100)].rstrip("\n"))
                else:
                    cont = False
                count += 1

        return self.words

    def run(self):
        print(self.getWords())


def listify():
    with open("./data/vocab.txt", "r") as god:
        words_listed = []
        for word in god:
            words_listed.append(word.rstrip("\n"))

        with open("./data/vocabList.txt", "w") as lord:
            lord.write(str(words_listed))

    return words_listed


def jsonify():
    with open("./data/vocabList.json", "w") as f:
        list = listify()
        json.dump(list, f)


# print(listify())
# jsonify()
godspeak(10)
