class chapte11Util:
    @staticmethod
    def readWordsDocAsDictionary():
        wordsDict = dict()
        fin = open('../Resources/words.txt')
        for line in fin:
            wordsDict[line.strip()] = line.strip()
        return wordsDict

    @staticmethod
    def readWordsDoc():
        words = []
        fin = open('../Resources/words.txt')
        for line in fin:
            words.append(line.strip())
        return words

