import requests

from bs4 import BeautifulSoup
from config import API_KEY
from main import saveData

def getData():

    urlLists = saveData()

    for url in urlLists:

        soup = requests.get(url)

        bs_obj = BeautifulSoup(soup.text, 'html.parser')

        p_obj = bs_obj.find_all('p')

        text = ''

        for p in p_obj:

            text += p.text

        makeRequestAndWriteFile(text)

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

    output = res.json()
    output = output['output']

    print(output)

getData()
