import pandas as pd
import numpy as np
import ast 
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity


ps = PorterStemmer()
cv = CountVectorizer(max_features=5000,stop_words='english')
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


def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    
    return " ".join(y)




def convert3(obj):
    temp = []
    count = 0
    for j in ast.literal_eval(obj):
        # print(j['name'])
        if not count == 3:
            temp.append(j['name'])
            count +=1
    return temp


def filtter_dir(obj):
    temp = []

    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            temp.append(i['name'])
            break
    
    return temp




filltred_df['genres'] = filltred_df['genres'].apply(convert)
filltred_df['keywords'] = filltred_df['keywords'].apply(convert)
filltred_df['cast'] = filltred_df['cast'].apply(convert3)
filltred_df['crew'] = filltred_df['crew'].apply(filtter_dir)
#print(filltred_df['keywords'])
filltred_df['crew'] = filltred_df['crew'].apply(lambda x : [i.replace(" ", "") for i in x] )
filltred_df['cast'] = filltred_df['cast'].apply(lambda x : [i.replace(" ", "") for i in x] )
filltred_df['keywords'] = filltred_df['keywords'].apply(lambda x : [i.replace(" ", "") for i in x] )
filltred_df['genres'] = filltred_df['genres'].apply(lambda x : [i.replace(" ", "") for i in x] )
filltred_df['overview'] = filltred_df['overview'].apply(lambda x: x.split())



filltred_df['Tags'] = filltred_df['overview'] + filltred_df['genres'] + filltred_df['keywords'] + filltred_df['cast'] + filltred_df['crew'] 

filltred_df['Tags'] = filltred_df['Tags'].apply(lambda x : " ".join(x))
filltred_df['Tags'] = filltred_df['Tags'].apply(lambda x : x.lower())
filltred_df['Tags'] = filltred_df['Tags'].apply(stem)
vectors = cv.fit_transform(filltred_df['Tags']).toarray()
simileraty = cosine_similarity(vectors).shape



def recommend(movie):
    movie_index = filltred_df[filltred_df['title'] == movie].index[0] 
    distances = simileraty[movie_index]
    movies_list = sorted(list(enumerate(simileraty[distances])),reverse=True,key=lambda x:x[1])[1:6]
    for i in movies_list:
        print(filltred_df.iloc[i[0]].title)  
      
    # cv.get_feature_names_out()
# print(cv.get_feature_names_out())

# print(vectors[0])


    
