# Movie-recommendation-01-
This is the ML first full project that is Movie recommendation system in am going to develop. 

## Types of recomendation system
1. Content Based 
2. Collabaretive fitering
3. Hybrid.

Content Based :- mainly recomendated on the bases on the content you are seeing . 

## Flow of project 
![alt text](image.png)

## About the data 
The database we chossen here is taken from the tmdb data set one is Mocies.csv and the Credits.csv
After download the data i read it using pandas and understood the dataset provided 

The columns i show in the Movies Dataset where
['budget', 'genres', 'homepage', 'id', 'keywords', 'original_language', 'original_title', 'overview', 'popularity', 'production_companies', 'production_countries', 'release_date', 'revenue', 'runtime', 'spoken_languages', 'status', 'tagline', 'title', 'vote_average', 'vote_count']


The columns i show in the Creidets in the dataset where 
['movie_id', 'title', 'cast', 'crew']

## Cleaning of the data

Sence we have a two data set lets first step will be to merge the two dataset as i saw the data i thing i can merdge the data set using column title .
so first setp is <b> "MERGING DATASET"</b>

Now coming to the next prosses i thought how would a human would recommand a movie to another human keeping the columns names to the referance that are 

['movie_id','title','overview','genres','cast', 'crew']

keeping this in point i am removing all other columns from the dataset we are having

Now I movied forword to the Pre-Prossing of the data One is to check weather any of the columns are having 'Null' value or not as sown below the as per columns and null value count in them

movie_id    0<br>
title       0<br>
overview    3<br>
genres      0<br>
cast        0<br>
crew        0<br>
sence <b> OverView</b> is very important column and i cant afford it to be NULL so sence the count of null value is not much i would like to drop those rows or say that data 

Now sence the Keyword and Overview is solved we should now go for column <b>cast</b> it looks something like this now <br>
{"cast_id": 242, "character": "Jake Sully", "credit_id": "5602a8a7c3a3685532001c9a", "gender": 2, "id": 65731, "name": "Sam Worthington", "order": 0}

we are just appending the names of the actor's top 3 one from the cast and appending in the list so the list may look some thing like this<br>
['Sam Worthington', 'Zoe Saldana', 'Sigourney Weaver']
 
Now the column crew should be prossed and the way i am going to prosses this column data is i am going to see the job weather the job is listed as Director if yes i am going to append it else not.<br>

one last step of the data proccessing is to remove the spaces form the words in the column such that there will be no Ambiguity and <b>Overview</b> is the column which is in the string should be in the list like any other columns in the dataframe so i converted in the list so that i can concat ithem all to make <b>Tag</b> column.

## Next step of data-Prossing
Sence the we cleard the shit in our data its time to male the data in right formate so that its becomes easy to prosses lets concat the columns and add a new column in the df called <b>Tag</b> and remove all other column , and convert the column back to string<br>
Just to make the data easy for the vectorization i would convert it all the <b>Tags</b> column data to the smaller

## Vectorization
The whole point here is to convert the each sentance of the tages to the vector, and how are we going to do it using concept <b>Bag of Words</b> <a>Bag of Words (BoW) is a fundamental technique in Natural Language Processing (NLP) that converts text into numerical features for machine learning models</a> In vectorization we will remove the <b>Stop Words</b> and we are going to do it using Sklearn to do vectorization 