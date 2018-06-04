import scraper

# Initialize end variables (arrays) from the scraper.
userIDs = scraper.userIDs
userNames = scraper.userNames
userDonations = scraper.userDonations
userTrophies = scraper.userTrophies


# Assign points to userID's based on trophies
def AssignTrophiesPoints(userIDs):
    userScoreFromTrophies = []
    for i in range(len(userIDs)):
        # Workaround for python's bad calculations
        score = (200 - (4 * i))
        score = score / 100
        userScoreFromTrophies.append(score)
    return userScoreFromTrophies


# Calculate score for a specific position n
def AssignDonationsPointByUserN(userDonations, n):
    counter = 0
    score = userDonations[n]
    for i in range(len(userDonations)):
        if score != userDonations[i]:
            if int(score) < int(userDonations[i]):
                counter = counter + 1
    points = 400 - (8 * counter)
    points = points / 100
    return points


# Assign points to userID's based on donations
def AssignDonationsPoints(userDonations):
    userScoreFromDonations = []
    for n in range(len(userDonations)):
        userScoreFromDonations.append(AssignDonationsPointByUserN(userDonations, n))
    return userScoreFromDonations


# Prints stats based on pos n in userIDs
def printSpelerStatsByID(n, userIDs, userNames, userDonations, userTrophies, userScoreFromDonations,
                         userScoreFromTrophies):
    print("Tag ID: " + userIDs[n])
    print("Username: " + userNames[n])
    print("Donaties: " + userDonations[n])
    print("Trofeen: " + userTrophies[n])
    print("Punten donaties: " + str(userScoreFromDonations[n]))
    print("Punten trofeeen: " + str(userScoreFromTrophies[n]))
    totaal = float(userScoreFromTrophies[n]) + float(userScoreFromDonations[n])
    print("Totaal: " + str(float(totaal)))


userScoreFromDonations = AssignDonationsPoints(userDonations)
userScoreFromTrophies = AssignTrophiesPoints(userIDs)

printSpelerStatsByID(2, userIDs, userNames, userDonations, userTrophies, userScoreFromDonations, userScoreFromTrophies)
