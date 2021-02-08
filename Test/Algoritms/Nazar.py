from pathlib import Path


def init_dict(src_file):
    with open(src_file, 'r', encoding='UTF-8') as dict_file:
        words = {word.strip(): dict() for word in dict_file}
        return words


def index_words_in_file(file, words):
    file_name = file if type(file) == str else file.name
    with open(file, 'r', encoding='UTF-8') as f:
        file_content = str(f.read()).lower()
        for word in words:
            words[word][str(file_name)] = word in file_content


def index_words(texts_dir, words):
    texts_dir = Path(texts_dir).glob("*.txt")
    for cur_file in texts_dir:
        index_words_in_file(cur_file, words)

    if __name__ == '__main__':
        word_dictionary = init_dict('C:/Users/tint4/laba 5/lemmDict.txt')
        index_words('C:/Users/tint4/laba 5/Files', word_dictionary)
        print(word_dictionary)
        query = input('Введите слово которое хотите найти')
        if query not in word_dictionary:
            print("Слово не найдено")
            exit (0)
        query_index = word_dictionary[query]
        for file, contains in query_index.items():
            if contains:
                print(file)