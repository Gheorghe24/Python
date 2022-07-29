#Write in a file

# file = open('data.txt', 'w') 
# try: 
#     file.write('ana are mere\n') 
# finally: 
#     file.close()

#Read from a file

# with open('data.txt', 'r') as f:
#     data = f.read()
#     print(data)


#Read from a file in a specific format(Csv)

# with open('netflix_titles.csv', 'r', encoding="utf-8") as f:
#     data = f.read()
#     print(data)

#This is not very useful

#We have a solution to store it tabular
from platform import release
import pandas as pd
df = pd.read_csv('netflix_titles.csv')

        