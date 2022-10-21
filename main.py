import requests
import nltk


#nltk.download('averaged_perceptron_tagger')


def get_text(url: str):

    # Проверяем, не пустой ли url
    if url != "":
        res = requests.get(url)

        speach_parts = [
            {
                "name": "Прилагательные",
                "amount": 0,
                "tags": ["JJ", "JJS", "JJR"]
            },
            {
                "name": "Предлоги",
                "amount": 0,
                "tags": ["IN", "TO"]
            },
            {
                "name": "Наречия",
                "amount": 0,
                "tags": ["RB", "RBS", "RBR", "WRB"]
            },
            {
                "name": "Союзы",
                "amount": 0,
                "tags": ["CC"]
            },
            {
                "name": "Артикли",
                "amount": 0,
                "tags": ["DT"]
            },
            {
                "name": "Существительные",
                "amount": 0,
                "tags": ["NN", "NNS", "NNP", "NNPS"]
            },
            {
                "name": "Числительные",
                "amount": 0,
                "tags": ["CD"]
            },
            {
                "name": "Местоимения",
                "amount": 0,
                "tags": ["PRP", "PRP$", "WP", "WP$"]
            },
            {
                "name": "Глаголы",
                "amount": 0,
                "tags": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
            }
        ]

        # Проверяем статус запроса
        if res.status_code == 200:

            # Токенезация текста, приведённого к utf-8
            words = nltk.word_tokenize(str(res.content.decode("utf-8")))

            # Помечаем токены тэгами
            tagged_words = nltk.pos_tag(words)

            for word in tagged_words:
                for speach_part in speach_parts:
                    if word[1] in speach_part["tags"]:
                        speach_part["amount"] +=1

            # Общее число слов
            sum = 0
            
            print("---===---")

            # Проходимся по отсортированному по количеству слов списку частей речи
            for speach_part in sorted(speach_parts, key=lambda x: x['amount'], reverse=True):
                print(speach_part["name"], ": ", speach_part["amount"])
                sum += speach_part["amount"]

            print("Всего: ", sum)

        else:
            print("Error: ", res.status_code)

    else:
        print("URL is empty")


if __name__ == "__main__":
    url = "https://gist.githubusercontent.com/nzhukov/b66c831ea88b4e5c4a044c952fb3e1ae/raw/7935e52297e2e85933e41d1fd16ed529f1e689f5/A%2520Brief%2520History%2520of%2520the%2520Web.txt"
    get_text(url)
