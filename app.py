from PyDictionary import PyDictionary
import argparse

parser = argparse.ArgumentParser(description="cli dictionary tool")
parser.add_argument("-w", "--word", metavar="word",
                    required=True, help="Enter the word")
args = parser.parse_args()

dictionary = PyDictionary()


word = args.word


def get_meanings(word):
    try:
        meanings = dictionary.meaning(word)["Noun"]
        for i in range(len(meanings)):
            print(f"{i+1}. {meanings[i]}")
    except Exception as e:
        print(f"Error: The Following Error occurred: {e}")


get_meanings(word)
