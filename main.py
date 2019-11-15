import webbrowser
import requests

from config import CONSUMER_KEY

def getData():

    headers = {
        'Content-Type': 'application/json',
        'X-Accept': 'application/json',
    }

    data = '{"consumer_key":"' + CONSUMER_KEY + '","redirect_uri":"http://www.google.com"}'

    response = requests.post('https://getpocket.com/v3/oauth/request', headers = headers, data = data, verify = False)

    jsonval = response.json()

    request_token = jsonval['code']

    print(request_token)

    webbrowser.open('https://getpocket.com/auth/authorize?request_token={0}&redirect_uri={1}'
    .format(request_token, 'https://google.com'))

    #data = '{"consumer_key":"1234-abcd1234abcd1234abcd1234","code":"dcba4321-dcba-4321-dcba-4321dc"}'

    data = '{"consumer_key":"' + CONSUMER_KEY + '","code":"' + request_token + '"}'

    response = requests.post('https://getpocket.com/v3/oauth/authorize', headers = headers, data = data, verify = False)

    jsonval = response.json()

    access_token = jsonval['access_token']

    print(access_token)

    data = '{"consumer_key":"' + CONSUMER_KEY + '", "access_token":"' + access_token + '"}'

    response = requests.post('https://getpocket.com/v3/get', headers = headers, data = data, verify = False)

    data =  response.json()

    return data
#data = None

# with open('val.json', 'w', encoding = 'utf-8') as file:
#
#     json.dump(response.json(), file, ensure_ascii=False, indent=4)

def saveData():

    data = getData()

    item_url = []
    item_title = []
    item_image_url = []
    not_articles = []
    count = 0

    for item in data['list']:

        count += 1

        if data['list'][item]['is_article'] != '1':

            not_articles.append(data['list'][item]['given_url'])
            continue

        try:
            item_url.append(data['list'][item]['given_url'])
        except:
            item_url.append("doesen't exist")
            pass

        try:
            item_title.append(data['list'][item]['given_title'])
        except:
            item_title.append("doesen't exist")
            pass

        try:
            item_image_url.append(data['list'][item]['top_image_url'])
        except:
            item_image_url.append("doesen't exist")
            pass

    for i in range(len(item_url)):

        # print("item_url: ", item_url[i])
        # print("item_title: ", item_title[i])
        # print("image_url: ", item_image_url[i])
        print("count: ", count)
        print(len(not_articles))
        print(not_articles)

    return item_url
