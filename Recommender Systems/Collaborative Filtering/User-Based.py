# A dictionary of movie critics and their ratings of a small
# set of movies
critics = {
    "Lisa Rose": {
        "Lady in the Water": 2.5,
        "Snakes on a Plane": 3.5,
        "Just My Luck": 3.0,
        "Superman Returns": 3.5,
        "You, Me and Dupree": 2.5,
        "The Night Listener": 3.0,
    },
    "Gene Seymour": {
        "Lady in the Water": 3.0,
        "Snakes on a Plane": 3.5,
        "Just My Luck": 1.5,
        "Superman Returns": 5.0,
        "The Night Listener": 3.0,
        "You, Me and Dupree": 3.5,
    },
    "Michael Phillips": {
        "Lady in the Water": 2.5,
        "Snakes on a Plane": 3.0,
        "Superman Returns": 3.5,
        "The Night Listener": 4.0,
    },
    "Claudia Puig": {
        "Snakes on a Plane": 3.5,
        "Just My Luck": 3.0,
        "The Night Listener": 4.5,
        "Superman Returns": 4.0,
        "You, Me and Dupree": 2.5,
    },
    "Mick LaSalle": {
        "Lady in the Water": 3.0,
        "Snakes on a Plane": 4.0,
        "Just My Luck": 2.0,
        "Superman Returns": 3.0,
        "The Night Listener": 3.0,
        "You, Me and Dupree": 2.0,
    },
    "Jack Matthews": {
        "Lady in the Water": 3.0,
        "Snakes on a Plane": 4.0,
        "The Night Listener": 3.0,
        "Superman Returns": 5.0,
        "You, Me and Dupree": 3.5,
    },
    "Toby": {
        "Snakes on a Plane": 4.5,
        "You, Me and Dupree": 1.0,
        "Superman Returns": 4.0,
    },
}

print(critics["Lisa Rose"]["Lady in the Water"])

"""
It words fine. Now we'll try to find the similar users.
After collecting data about the things people like, you need a way to determine how similar people are
in their tastes. You do this by comparing each person with every other person and then calculating a
similarity score. Here, we'll discuss two methods to calculate the similarity score: Euclidean distance
and Pearson correlation.

Euclidean Method: In this it takes the items that people have rated on axis and put the ratings respectively.
"""

from math import sqrt


def sim_distance(prefs, person1, person2):
    """
    Returns a distance based similarity score.
    """

    # Get the list of shared_items
    si = {}

    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # if they have no ratings in common, return 0
    if len(si) == 0:
        return 0

    # Add up the squares of all the differences

    sum_of_squares = sum(
        [
            pow(prefs[person1][item] - prefs[person2][item], 2)
            for item in prefs[person1]
            if item in prefs[person2]
        ]
    )

    return 1 / (1 + sum_of_squares)


print(
    "The Euclidean Score is: {}".format(
        sim_distance(critics, "Lisa Rose", "Gene Seymour")
    )
)
print(
    "The Euclidean Score is: {}".format(
        sim_distance(critics, "Lisa Rose", "Claudia Puig")
    )
)
print(
    "The Euclidean Score is: {}".format(
        (sim_distance(critics, "Lisa Rose", "Michael Phillips"))
    )
)
print("The Euclidean Score is: {}".format(sim_distance(critics, "Lisa Rose", "Toby")))

"""
Peasrson Correlation Score: It is a measure of how well two sets of data fit on a straight line. 
It tends to give better results in situations where the data is not normalized. It gives you answers
between -1 and 1. 1 means both critics have given the same ratings.
"""


def sim_pearson(prefs, p1, p2):
    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    # Find the number of elements
    n = len(si)
    # if they are no ratings in common, return 0
    if n == 0:
        return 0
    # Add up all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    # Sum up the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
    # Sum up the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])
    # Calculate Pearson score
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r


print(
    "The Pearon score is: {}".format(sim_pearson(critics, "Lisa Rose", "Gene Seymour"))
)
print(
    "The Pearon score is: {}".format(sim_pearson(critics, "Lisa Rose", "Claudia Puig"))
)
print(
    "The Pearon score is: {}".format(
        sim_pearson(critics, "Lisa Rose", "Michael Phillips")
    )
)
print("The Pearon score is: {}".format(sim_pearson(critics, "Lisa Rose", "Toby")))

"""
Ranking the critics.
"""


def topMatches(prefs, person, n=5, similarity=sim_pearson):

    scores = [
        (similarity(prefs, person, other), other) for other in prefs if other != person
    ]

    # Sort the list so the highest scores appear at the top

    scores.sort()
    scores.reverse()

    return scores[0:n]


print(topMatches(critics, "Toby"))


"""
Recommending Items
"""
# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(prefs, person, similarity=sim_pearson):

    totals = {}
    simSums = {}

    for other in prefs:
        # don't compare me to myself
        if other == person:
            continue

        sim = similarity(prefs, person, other)

        # ignore scores of zero or lower
        if sim <= 0:
            continue

        for item in prefs[other]:
            # only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:

                # Similarity * Score
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim

                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim

    # Create the normalized list
    rankings = [(total / simSums[item], item) for item, total in totals.items()]

    # Return the sorted list
    rankings.sort()
    rankings.reverse()

    return rankings


print(getRecommendations(critics, "Toby"))

"""
This code loops through every other person in the prefs dictionary. In each case, it calculates how similar
they are to the person specified. It then loops through every item for which they have given a score. The 
score for each item is multilplied by the similarity and these products are all added together. At the end,
the scores are normalized by dividing each of them by similarity sum, and the sorted results are returned.
Not only you get a list of recommended movies but you also get what your approximate rating would be for the 
respective movies. This rankning decides if I should watch the movie at all or should I do something else entirely.
"""

"""
Matching Products

In this case you can define similarity by looking at who liked a particular item and looking at the other 
items they've liked. This is actually the same method that we used to calculate the similarity with distance.
We just need to swap the people and the items.
"""


def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})

            # Flip item and person
            result[item][person] = prefs[person][item]
    return result


movies = transformPrefs(critics)
print("Top Mathces :\n............\n", topMatches(movies, "Superman Returns"))
print("Recommendations :\n..............\n", getRecommendations(movies, "Just My Luck"))

"""
The way the recommendation engine has been implemented so far requires the use of all the ranking from every
user in order to creat the dataset. This will probably work well for thousands of people or items. But a very
large site like Amazon has millions of customers and products. Comparing a user with every other user or 
comparing a product with every other product that user has rated can be very slow. Also, a site that sells 
millions of products may have very little overlap between people, which can make it difficult to decide 
which people are similar.

The technique we have used here is called user-based collaborative filtering and an alternative of this is
item-based collaborative filtering. In cases with very large datasets, item-based collaborative filtering 
can give better results, and it allows many of the calculations to be performed in advance so that a user
needing recommendations can get them more quickly.

The general technique is to pre-calculate the most similar items for each item. Then when you wish to make the
recommendations to a user, you look at his/her top rated items and create a weighted list of the items most
similar to them. The important difference here is that, although the first step requires you to examine
all the data, comparisons between items will not change as often as comparisons between users.

"""
