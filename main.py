import tkinter.messagebox
from types import NoneType

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

file = "csv/cocktails_data.csv"
df = pd.read_csv(file)

#  Create a TF-IDF Object
v = TfidfVectorizer()

df['Cocktail Name'].fillna('')
df['Ingredients'].fillna('')
df['Garnish'].fillna('')

vecMatrix = v.fit_transform(df['Ingredients'])

#  Cosine similarity score
cos = linear_kernel(vecMatrix)

#  Creates one-dimensional list of cocktail names and their indices
indexList = pd.Series(df.index, index=df['Cocktail Name'])


def getRecommendedDrinks(cocktailName, cosine=cos):
    try:
        id = indexList[cocktailName]
        similarityScores = list(enumerate(cosine[id]))
        similarityScores = sorted(similarityScores, key=lambda x: x[1], reverse=True)

        # Get the top 5 similar cocktails
        similarityScores = similarityScores[1:6]
        cocktailIndices = [index[0] for index in similarityScores]
        topFiveSimScores = [index[1] for index in similarityScores]

        topFive = df['Cocktail Name'].iloc[cocktailIndices].to_list()

        #  Displays bar graph for top five similar cocktails
        # plt.title(f'Top Five Similar Cocktails - {cocktailName}')
        # plt.xlabel('Similar Cocktails')
        # plt.ylabel('Similarity Scores')
        # plt.bar(topFive, topFiveSimScores)
        # plt.show()

        return topFive, cocktailIndices

    except KeyError:
        invalidName()


def printDrinks(topFive):
    print(f'{topFive[0]}\n{topFive[1]}\n{topFive[2]}\n{topFive[3]}\n{topFive[4]}')


def invalidName():
    tkinter.messagebox.showerror("Cocktail Not Found",
                                 "There is no cocktail with that name in this database. Please choose another.")
