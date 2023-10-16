# API_TO_POSTGRESQL

## I. Introduction
### 1. The gold of this project
This project is to build a simple ETL pipeline to fetch real-time data from an open source API and store that data into a database. For this case I have used Yelp FUSION API as the open source API available and for database I used Postgres and used Docker to deloy application.

## II. Detail File
### 1. Config File
```
[KEYS]
API_KEY=<YOUR API KEY>


[DATABASE]
host=<HOST NAME>
database=<DB NAME>
username=<USER NAME>
password=<PASSWORD>
port=<PORT>

```


### 2. File
```
auth.py - Contains configuration variable for making HTTP Request

foodsearch.py - Contains class to handle results returned from the search request

databasedriver.py - Contains Connection detials to Postgres database and executing queries

queries.py - Contains queries to create schema and tables in postgres and insert statement format

request.py - Contains class to handle making request to the API

driver.py - Entry point for the application, contains parsing command line arguments and control the program flow.
```

## II. Deploy
```
  Folder:
        Docker:
              .env - Contains parameters to deloy postgresql ( i.e: POSTGRES_USER=<USER NAME>
                                                                    POSTGRES_PORT=<PORT> )
              docker-compose.yml - Deloy PostgreSQL with Network: ete_network
```

## How To Run
  I use Makefiles for all my projects to have a way to install and run them
  Makefile:
        To compile each, run the following commands:
            To run container Postgresql with : 
            ``
                  make up
            ``
            To stop container Postgresql with : 
            ``
                  make down
            ``
            To restart container Postgresql with : 
            ``
                  make restart
            ``
            To run application with : 
            ``
                  make run
            ``
            make run is equivalent to `python driver.py --term food --location 'United States' --price 1` 



## Results
![RESULTS](https://github.com/san089/Udacity-Data-Engineering-Projects/blob/master/Data_Api_to_Postgres/Results.PNG)
