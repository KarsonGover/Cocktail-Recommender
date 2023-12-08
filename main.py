import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

file = "csv/cocktails_data.csv"
df = pd.read_csv(file)

#  Create a TF-IDF Object
vectorizer = TfidfVectorizer()

df['Cocktail Name'].fillna('')
df['Ingredients'].fillna('')
df['Garnish'].fillna('')

vecMatrix = vectorizer.fit_transform(df['Ingredients'])

#  Cosine similarity score
cos = linear_kernel(vecMatrix)

#  Creates one-dimensional list of cocktail names and their indices
indexList = pd.Series(df.index, index=df['Cocktail Name']).drop_duplicates()


def getRecommendedDrinks(cocktailName, cosine=cos):
    id = indexList[cocktailName]
    similarityScores = list(enumerate(cosine[id]))
    similarityScores = sorted(similarityScores, key=lambda x: x[1], reverse=True)

    # Get the top 5 similar cocktails
    similarityScores = similarityScores[1:6]
    cocktailIndices = [index[0] for index in similarityScores]

    topFive = df['Cocktail Name'].iloc[cocktailIndices].to_list()
    printDrinks(topFive)


def printDrinks(topFive):
    print(f'{topFive[0]}\n{topFive[1]}\n{topFive[2]}\n{topFive[3]}\n{topFive[4]}')


getRecommendedDrinks("Off the Radar")
