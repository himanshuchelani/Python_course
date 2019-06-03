"""
Code Challenge
Name:
    IGN Analysis
Filename:
    ign.py
Problem Statement:
    Read the ign.csv file and perform the following task :

        Let's say we want to find games released for the Xbox One
        that have a score of more than 7.

    review distribution for the Xbox One vs the review distribution
    for the PlayStation 4.We can do this via a histogram, which will plot the
    frequencies for different score ranges.



Hint:

    The columns contain information about that game:

        score_phrase — how IGN described the game in one word.
        This is linked to the score it received.
        title — the name of the game.
        url — the URL where you can see the full review.
        platform — the platform the game was reviewed on (PC, PS4, etc).
        score — the score for the game, from 1.0 to 10.0.
        genre — the genre of the game.
        editors_choice — N if the game wasn't an editor's choice, Y if it was. This is tied to score.
        release_year — the year the game was released.
        release_month — the month the game was released.
        release_day — the day the game was released.


"""

# Importing the preprocessing and visualization modules
import pandas as pd


# Importing suppress from contextlib to handle exceptions
from contextlib import suppress

# Preprocessing stage
with suppress((FileNotFoundError)):

    # Loading the ign datasets
    ign_df = pd.read_csv("ign.csv")
    ign_df = ign_df.iloc[:,1:]

    # finding games released for the Xbox One that have a score of more than 7.
    xbox1_sc7_find = ign_df[(ign_df['platform']=="Xbox One") & (ign_df['score']>7)]

    # Finding the games for Xbox one platform and PlayStation 4
    allgames_platform = ign_df.groupby('platform')['score_phrase'].value_counts().unstack().fillna(0)

    # To perfrom visualization by histogram
    xbox_visual = ign_df['score'][ign_df['platform']=="Xbox One"].plot.hist()
    ps4_visual = ign_df['score'][ign_df['platform']=="PlayStation 4"].plot.hist()
