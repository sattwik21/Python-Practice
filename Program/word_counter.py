# Python program to get word and character count from a given input string
# Contributed by Ahamed Ruyefa DF


def getWordCount(str):
    return len(str.strip().split())


def getCharacterCount(str):
    return len(str.strip())


if __name__ == "__main__":
    userString = input("Enter string: ")
    wordCount = getWordCount(userString)
    characterCount = getCharacterCount(userString)
    print("Word count: ", wordCount)
    print("Character count: ", characterCount)
