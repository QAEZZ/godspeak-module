import random
import json


class god():

    def __init__(self):
        print("available commands:\n\ngod.speak()\ngod.quote()\n")

    class speak():

        def __init__(self, amount: int = 0, return_as_list: bool = True) -> "The holy words of God":
            """Returns the holy word of God"""
            self.amount = amount
            self.return_as_list = return_as_list

            if self.amount == 0:
                return "amount cannot be 0!"

            self.run()

        def getWords(self, return_as_list: bool = True):
            with open("./data/vocabList.json", "r") as god:
                data = json.load(god)
                #print(data)
                self.words = []
                count = 0
                cont = True
                while cont is True:
                    if count < self.amount:
                        self.words.append(data[random.randint(
                            0, 7568)].rstrip("\n"))
                    else:
                        cont = False
                    count += 1

            if return_as_list is True:
                return self.words
            else:
                final = ""
                for items in self.words:
                    final += items + " "
                return final

        def run(self):
            print(self.getWords(self.return_as_list))

    class quote():

        def __init__(self):
            print("Soon(TM)")


def listify(write_file=False):
    with open("./data/vocab.txt", "r") as god:
        words_listed = []
        for word in god:
            words_listed.append(word.rstrip("\n"))

        if write_file is True:
            with open("./data/vocabList.txt", "w") as lord:
                lord.write(str(words_listed))

    return words_listed


def jsonify():
    with open("./data/vocabList.json", "w") as f:
        list = listify()
        json.dump(list, f)
