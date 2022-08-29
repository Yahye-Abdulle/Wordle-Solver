import nltk
from nltk.corpus import words

class wordle:

    def __init__(self):
        self.word = ["","","","",""]
        self.wordC = 0
        self.remove = []
        self.removeC = 0
        self.contain = []
        self.dictionary = []
        self.possible = {}
        # Oxford Dictionary Frequency
        #self.freq = {"a" : 8.4966, "b": 2.0720,"c": 4.5388,"d": 3.3844,"e": 11.1607,"f": 1.8121,"g": 2.4705,"h": 3.0034,"i": 7.5448,"j": 0.1965,"k": 1.1016,"l": 5.4893,"m": 3.0129,"n": 6.6544,"o": 7.1635,"p": 3.1671,"q": 0.1962,"r": 7.5809,"s": 5.7351,"t": 6.9509,"u": 3.6308,"v": 1.0074,"w": 1.2899,"x": 0.2902,"y": 1.7779,"z": 0.2722}
        # Wikipedia Frequency
        self.freq = {"a" : 0.082, "b": 0.015,"c": 0.028,"d": 0.043,"e": 0.13,"f": 0.022,"g": 0.02,"h": 0.061,"i": 0.07,"j": 0.0015,"k": 0.0077,"l": 0.04,"m": 0.025,"n": 0.067,"o": 0.075,"p": 0.019,"q": 0.00095,"r": 0.06,"s": 0.063,"t": 0.091,"u": 0.028,"v": 0.0098,"w": 0.024,"x": 0.0015,"y": 0.02,"z": 0.00074}
        self.setup()
        self.display()
        self.run()

    def setup(self):
        for wrd in words.words():
            if len(wrd) == 5:
                self.dictionary.append(wrd)

    def run(self):
        for i in range(6):
            self.executeOne()
            print(self.word)
            print(self.remove)
            print(len(self.remove))
            self.runWordle()
            print(self.possible)
            self.reset()
            
    def reset(self):
        self.word = ["","","","",""]
        self.wordC = 0
        self.contain = []
        self.possible = {}
        self.removeC = 0
        
    def display(self):
        print("_ for grey \n- for yellow \n/ for green")

    def executeOne(self):
        tempRemove = ["","","","",""]
        wrd = list(input("Input word > "))
        result = list(input("Result > "))
        #wrd = ['w','e','a','r','y']
        #result = ['_', '-', '/', '-', '_']
        for i in range(len(wrd)):
            if result[i] == "/":
                self.word[i] = wrd[i]
                self.wordC += 1
            elif result[i] == "-":
                self.contain.append(wrd[i])
            elif result[i] == "_":
                tempRemove[i]= wrd[i]
                self.removeC += 1
        self.remove.append(tempRemove)

    def runWordle(self):
        for wrd in self.dictionary:
            if self.validateGrey(wrd.lower()): 
                if self.validateGreen(wrd.lower()):
                    if self.validateYellow(wrd.lower()):
                            self.possible[wrd] = self.calc(wrd.lower())
        #self.validateGrey()
        self.possible = {k: v for k, v in reversed(sorted(self.possible.items(), key=lambda item: item[1]))}

    
    def validateGrey(self, wrd):
        for i in range(len(self.remove)):
            for j in range(len(self.remove[i])):
                if self.remove[i][j] != "":
                    if list(wrd)[j] == self.remove[i][j]:
                        return False
        return True
    '''

    def validateGrey(self):
        count = 0
        for key, value in self.possible.items():
            print(key, value)
            for i in range(len(self.remove)):
                current = self.remove[i]
                for j in range(len(current)):
                    if list(key)[j] != current[j]:
                        count += 1
        if count == self.removeC:
            print("yes")
        '''
    def validateGreen(self, wrd):
        count = 0
        for i in range(len(self.word)):
            if self.word[i] != "":
                if list(wrd)[i] == self.word[i]:
                    count += 1
        if count == self.wordC:
            return True
        return False

    def validateYellow(self, wrd):
        count = 0
        for i in range(len(self.contain)):
            if self.contain[i] in list(wrd):
                count += 1

        if count == len(self.contain):
            return True
        return False

    def calc(self, wrd):
        score = 0
        for i in range(len(wrd)):
            score += self.freq.get(wrd[i])
        return score
        
        

X = wordle()

