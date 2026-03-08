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
