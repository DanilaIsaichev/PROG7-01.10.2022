import requests
import nltk

def get_text(url: str):
    
    if str != "":
        res = requests.get(url)

        list_of_speach_types = [{"name": "Прилагательные", "amount": 0, "value": "ADJ"},
            {"name": "Предлоги (адлоги)", "amount": 0, "value": "ADP"},
            {"name": "Наречия", "amount": 0, "value": "ADV"},
            {"name": "Союзы", "amount": 0, "value": "CONJ"},
            {"name": "Артикли", "amount": 0, "value": "DET"},
            {"name": "Существительные", "amount": 0, "value": "NOUN"},
            {"name": "Числительные", "amount": 0, "value": "NUM"},
            {"name": "Предлог", "amount": 0, "value": "PRT"},
            {"name": "Местоимения", "amount": 0, "value": "PRON"},
            {"name": "Глаголы", "amount": 0, "value": "VERB"}
            ]
        if res.status_code == 200:
            nltk.word_tokenize(str(res.content.decode("utf-8")))
            list_of_words = nltk.corpus.brown.tagged_words(tagset='universal')
            for word in list_of_words:
                for speach_type in list_of_speach_types:
                    if word[1] == speach_type["value"]:
                        speach_type["amount"] +=1

            for speach_type in sorted(list_of_speach_types, key=lambda x: x['amount'], reverse=True)[:5]:
                print(speach_type["name"], ": ", speach_type["amount"])
        else:
            print("error")
    else:
        print("error")


if __name__ == "__main__":
    get_text("https://gist.githubusercontent.com/nzhukov/b66c831ea88b4e5c4a044c952fb3e1ae/raw/7935e52297e2e85933e41d1fd16ed529f1e689f5/A%2520Brief%2520History%2520of%2520the%2520Web.txt")
