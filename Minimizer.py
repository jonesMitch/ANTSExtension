import tokenizer
import json
import sys

def loadConfig() -> dict:
    with open("config.json", "r") as file:
        configData = json.load(file)
    return configData

def minimize(configData: dict, readFileName):
    readPath = configData["filepaths"]["readPath"]
    writeFileName = "minimized" + readFileName
    writePath = configData["filepaths"]["writePath"]

    readFile = tokenizer.Tokenizer(f"{readPath}/{readFileName}")
    tokens = readFile.getTokens()

    newFileString = _formatOutput(tokens)
    with open(f"{writePath}/{writeFileName}", "w") as newFile:
        newFile.write(newFileString)

def _formatOutput(tokens: list) -> str:
    returnString = ""
    for token in tokens:
        returnString += f"{token} "
    return returnString

if __name__ == "__main__":
    arguments = sys.argv
    readFileName = "body.lua"
    if len(arguments) >= 2:
        readFileName = arguments[1]

    configData = loadConfig()
    minimize(configData, readFileName)
