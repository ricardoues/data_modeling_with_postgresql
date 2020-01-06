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


