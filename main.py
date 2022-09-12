import random
import json


class godspeak():

    def __init__(self, amount: int, return_type: str = "list"):
        self.amount = amount
        self.return_type = return_type
        self.return_as_list = return_as_list

        print(f"ready\namount: {self.amount}")
        self.run()
    
    def handleAndResolveReturnType(self, self.return_type):
        if self.return_type != "list" or "string":
            return f"\"{self.return_type}\" is not a valid return type! \"list\" and \"string\" are valid return types"
        else:
            if self.return_type == "list":
                self.return_as_list = True
            elif self.return_type == "string":
                self.return_as_list = False

    def getWords(self, self.return_as_list: bool = True):
        with open("./data/vocabList.json", "r") as god:
            data = json.load(god)
            #print(data)
            self.words = []
            count = 0
            cont = True
            while cont is True:
                if count < self.amount:
                    self.words.append(data[random.randint(0, 7568)].rstrip("\n"))
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
        self.handleAndResolveReturnType()
        print(self.getWords(self.return_as_list=self.return_type))


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


# print(listify())
# jsonify()
godspeak(10)
