class StringReader:
    def __init__(self, line: str, delimiter = " ", startIndex = 0):
        self.line = f"{StringReader._strip(line, delimiter)}{delimiter}"
        self.delimiter = delimiter
        self.startIndex = startIndex
        self.hasNextValue = True

    def next(self) -> str | None:
        """Returns the the next substring from the line that ends in the delimiter, or None if EOF"""
        if not self.hasNextValue:
            return None
        for char in range(self.startIndex, len(self.line)):
            if self.line[char] == self.delimiter:
                returnString = self.line[self.startIndex:char]
                self.startIndex = self._checkForDelimiters(char)
                return returnString
        return self.line[self.startIndex:]
                
    def _checkForDelimiters(self, endIndex) -> int:
        """Returns the index of the next non-delimiter character in the line"""
        if endIndex == len(self.line) - 1:
            self.hasNextValue = False
        for char in range(endIndex, len(self.line)):
            if self.line[char] != self.delimiter:
                return char

    def hasNext(self):
        return self.hasNextValue
    
    def _strip(line: str, delimiter: str) -> str:
        """Strips all leading and trailing delimiters from the line"""
        inMiddle = False
        middleStart = -1
        middleEnd = -1
        for char in range(0, len(line)):
            if line[char] != delimiter:
                middleStart = char
                break
        for char in reversed(range(0, len(line))):
            if line[char] != delimiter:
                middleEnd = char
                break
        return line[middleStart:middleEnd+1] 