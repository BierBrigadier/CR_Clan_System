import requests
import re

clanpageresponse = requests.get('http://statsroyale.com/clan/9QPRPQY').text.strip()


def GetUserNameByID(id):
    # Match: '>xxxxx</
    regex = 'https://statsroyale.com/profile/' + id + '\'>(.*?)</'
    username = re.search(regex, clanpageresponse).group(1)
    return username


def GetUserIDs():
    # Match: <a class=" ui__blueLink" href=' https://statsroyale.com/profile/xxxx'>
    userids = re.findall('https://statsroyale.com/profile/(.*?)\'', clanpageresponse)
    return userids


def GetUserNames(userids):
    usernames = []
    for i in range(len(userids)):
        username = GetUserNameByID(userids[i])
        usernames.append(username)
    return usernames


def GetUserDonations():
    # Match: 'clan__donation"> xxxxx </div>
    regex = 'clan__donation">(.*?)</'
    donations = re.findall(regex, clanpageresponse)
    return donations


def GetUserTrophies():
    # Match: 'clan__cup"> xxxxx </div>
    regex = 'clan__cup">(.*?)</'
    trophies = re.findall(regex, clanpageresponse)
    return trophies


userIDs = GetUserIDs()
userNames = GetUserNames(userIDs)
userDonations = GetUserDonations()
userTrophies = GetUserTrophies()
