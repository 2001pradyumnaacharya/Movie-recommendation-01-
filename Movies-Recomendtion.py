import pandas as pd
import numpy as np
import ast 

# Creating dataFrame of movies
movies_data_df = pd.read_csv(r"/home/pradyumna/MLProjects/Movie-recommendation-01-/tmdb_5000_movies.csv")
credts_data_df = pd.read_csv(r"/home/pradyumna/MLProjects/Movie-recommendation-01-/tmdb_5000_credits.csv")

# print("movies dataSet")
# print(movies_data_df.columns.to_list())
# print("-"*20)
# print("credits dataSet")
# print(credts_data_df.columns.to_list())

main_df = movies_data_df.merge(credts_data_df, on=['title'])
filltred_df = main_df[['movie_id','title','overview','genres','keywords','cast', 'crew']]

# print(filltred_df.isnull().sum())

filltred_df = filltred_df.dropna()
#print(filltred_df.isnull().sum())


def convert(obj):
    temp = []
    
    for j in ast.literal_eval(obj):
        # print(j['name'])
        temp.append(j['name'])
    return temp


filltred_df['genres'] = filltred_df['genres'].apply(convert)
filltred_df['keywords'] = filltred_df['keywords'].apply(convert)

print(filltred_df['keywords'])

    
