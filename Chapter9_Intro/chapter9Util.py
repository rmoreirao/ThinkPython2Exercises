class chapter9Util:
    @staticmethod
    def readWordsDoc():
        words = []
        fin = open('words.txt')
        for line in fin:
            words.append(line.strip())
        return words

