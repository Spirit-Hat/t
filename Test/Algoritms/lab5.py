#1.	Розробити індексатор з бінарною моделлю текстових документів.
from pathlib import Path
import time

start_time = time.time()

def Load_Dict():
    with open("dict.txt", 'r', encoding='UTF-8') as dicts:
        words=dict()
        for word in dicts:
             words[word.strip()] = ""
        return words
def ReadFiles(dicts):
    path=r'C:\Users\Vlad\PycharmProjects\Test\Algoritms\Files'
    words = dict(dicts)
    file = Path(path).glob("*.txt")
    for cur_file in file:
        with open(cur_file, 'r', encoding='UTF-8') as data:
            data_files=data.read()
            data_files=data_files.split("\n")
            for word in data_files:
                try:
                    words[word]

                    words.update({word: cur_file})
                except KeyError as e:
                    pass

    return words
if __name__=='__main__':
    Dict=Load_Dict()
    print(Dict)
    Dict=ReadFiles(Dict)
    print(Dict)
    words = dict(Dict)
    EnterData = input('Enter the word you want to find\n')
    try:
        words[EnterData]
        if  words[EnterData] !="":
            print("Word found")
            print(words[EnterData])
            print("--- %s seconds ---" % (time.time() - start_time))
        else:
            print("Word not found")
            print("--- %s seconds ---" % (time.time() - start_time))
    except KeyError as e:
        print("Word not found")
        print("--- %s seconds ---" % (time.time() - start_time))
