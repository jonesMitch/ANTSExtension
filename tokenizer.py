import stringReader as SR

class Tokenizer:
    def __init__(self, filePath: str):
        self.filePath = filePath
        self.tokens = []

    def getTokens(self) -> list:
        """Returns a list of all tokens in the file, in order"""
        with open(self.filePath, "r") as file:
            for line in file:
                lineReader = SR.StringReader(line)
                while lineReader.hasNext():
                    self.tokens.append(lineReader.next())
        return self._cleanTokens()
    
    def _cleanTokens(self):
        cleanedTokens = []
        for token in self.tokens:
            if token[-1] == "\n":
                cleanedTokens.append(token[0:-1])
            else:
                cleanedTokens.append(token)
        return cleanedTokens