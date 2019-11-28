import requests

from bs4 import BeautifulSoup
from config import API_KEY
from main import saveData

def getData():

    data = saveData()
    titles = data[0]
    print(titles[0:15])
    urlLists = data[1]
    summarizedArticles = []
    summarizedData = []

    urlTest = urlLists[0 : 15]
    i = 0

    for url in urlTest:

        soup = requests.get(url)

        bs_obj = BeautifulSoup(soup.text, 'html.parser')

        p_obj = bs_obj.find_all('p')

        text = ''

        for p in p_obj:

            text += p.text

        i += 1
        summary = makeRequestAndWriteFile(text)
        summarizedArticles.append(summary)
        print("got data", i)

    summarizedData.append(summarizedArticles)
    summarizedData.append(titles)

    return summarizedData

def makeRequestAndWriteFile(text):

    res = requests.post(
                        "https://api.deepai.org/api/summarization",
                        data = {'text' : text},
                        headers = {'api-key' : API_KEY}
                        )

    # with open('val3.txt', 'w', encoding = 'utf-8') as file:
    #
    #     #json.dump(res.json(), file, ensure_ascii = False, indent = 2)
    #     output = res.json()
    #     output = output['output']
    #
    #     file.write(output)

    try:
        output = res.json()
        output = output['output']
    except:
        output = "None"

    return output
