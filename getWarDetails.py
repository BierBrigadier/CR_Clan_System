import requests
import re
import pprint

url = "https://api.royaleapi.com/clan/9QPRPQY/warlog"

headers = {
    'auth': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Mzc0LCJpZGVuIjoiMjAyMzQ5NTY3ODgxMTE3Njk2IiwibWQiOnt9LCJ0cyI6MTUyODEyMzg1MDE2N30.Pqy-JmrMHp-oiNyp9Gra6dTTxnj6ue_66EA7a5oLj20
"
}
response = requests.request("GET", url, headers=headers)
data = response.json()


def getWars():
    # match: 'createdDate': XXXXXXXXXXX  }]},
    regex = '\'createdDate\':(.*?)}, {\''
    wars = re.findall(regex, str(data))
    return wars


def CompareWars(war1, war2):
    # match: XXXXXXXXXX', 'participants'
    regex = ' (.*?), \'participants'
    warstamp1 = re.findall(regex, str(war1))
    warstamp2 = re.findall(regex, str(war2))
    if war1 == war2:
        return True
    return False



# match: 'name': 'Svennos'   XXXXXXXX },
regex = '\'name\': \'Svennos\'(.*?)},'
donations = re.findall(regex, str(data))

print(data)
# pprint.pprint(getWars())

print(getWars()[0])
print(len(getWars()))

# pprint.pprint(donations)
