# Introduction
This is a project provided by Udacity and the goal of this project is to apply data modeling in the startup called Sparkify which provides a streaming service like Spotify. We will use fact and dimension tables in order to organize the data. Finally, we will build a ETL pipeline to process the song and log files. 

# Purpose of the project 
Sparkify is a startup that provides a music streaming service similar to Spotify. Sparkify collects data from its users through log files. In order to provide valuable information to the analytic team, we created dimension and fact tables for a [star schema](https://en.wikipedia.org/wiki/Star_schema). A star schema is a methodology to develop databases which consists of one or more fact tables referencing any number of dimension tables.

With the PostgreSQL database, we will analyze the song that the users play in order to find insights. Then, we will implement a recommendation system in order to provide a better user experience, and with this keeping a high level of people that uses Sparkify daily. 


# Justifying the database schema 

The database schema includes the following dimension tables:

* users: users in the app
* songs: songs in music database
* artists: artists in music database
* time: timestamps of records in songplays broken down into specific units

And the following fact table: 

* songplays: records in log data associated with song plays i.e. records with page NextSong.

This schema is very convenient since that with the fact table we can get the information that we need to get insights from the song that the users play without the needing of doing any kind of join.  


# Files 
The project has the following files: 

* test.ipynb displays the first few rows of each table to let you check your database.
* create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
* etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
* etl.py reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
* sql_queries.py contains all your sql queries, and is imported into the last three files above.
* README.md provides discussion on your project.

# How to run the code 
You must have postgreSQL 9.5 or greater installed in your computer, moreover you must have
Python 3.6 or greater installed in your computer. In the file requirements.txt there is a list of the packages that you must install in your computer in order to run the codes properly.

Below are steps you can follow to run the codes:

* Run from a terminal create_tables.py to create your database and tables.
* Run from a terminal etl.py to run the ETL pipeline that load the data into postgreSQL tables.
* Run using jupyter notebook the file test.ipynb to confirm the result of running the ETL pipeline.

