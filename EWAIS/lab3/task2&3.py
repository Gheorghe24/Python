from platform import release
import pandas as pd

df = pd.read_csv('netflix_titles.csv')

# get the data by column and convert to a list

df = df.sort_values(by="release_year")
titles = list(df["title"])
release = list(df["release_year"])

#Now I have the tiles sorted by release year in a list
#So I write the list in a new file

n_titles = len(titles)
n_release = len(release)

with open("titles.txt", "w", encoding="utf-8") as file:
    for i in range(n_titles):
        file.write(titles[i] + " " + str(release[i]) + "\n")