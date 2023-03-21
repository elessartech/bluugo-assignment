# Bluugo Assignment

## Installation instructions

### Docker 

The app can be installed using Docker. In order to do that one must have [Docker]('https://docs.docker.com/get-docker/') and [docker-compose]('https://docs.docker.com/compose/install/') installed on the machine. 
- Go to the root directory of the app and execute
```
docker-compose up
```
- Once the installation has been completed head over to the http://localhost:5000 in your browser. 


### Local

- Install and configure PostgresQL. Instructions can be found [here]('https://www.postgresql.org/download/').
- Clone the repository `git clone https://github.com/elessartech/bluugo-assignment.git`
- Head over to the root directory
- SQL schemas used for the app can be found at `schema.sql`. Define tables by either PostgreSQL-CI or pgAdmin. [Instructions can be found here]('https://www.javatpoint.com/postgresql-create-table').
- Create virtual environment `python3 -m venv venv`
- Activate it `source venv/bin/activate` 
- Install all required packages `pip install -r requirements.txt`
- Create `.env`-file and add there required variables:

| Key | value |
| ------ | ------ |
| DATABASE_URL  | postgresql://${username}:${password}@${host}:${port}/${database} |
| SECRET_KEY | ${YOUR_SECRET_KEY} |
| FLASK_APP | app |
| FLASK_DEBUG | True/False |
- Run `flask run` to run the app
- Go to `http://localhost:5000` in your browser.

## Functionality 

- ✅User must be able to upload a JSON file [vehicle_data.json]('https://tracking.cloud/documents/2/vehicle_data.json) via form.

- ✅Uploaded data must be stored in a relational database. 

- ✅Recurring uploads must update existing database rows (instead of duplicating the data).

- ✅User must be able to search existing database rows by using a free text search box. 

- ✅Search must be on the same page as the upload form.

- ✅Search must be implemented as a “live” search, meaning that the search is listening for user input and the page doesn’t reload in between searches.

- ✅Search results must be limited to 50.

- ✅The frontend of the application must be implemented without the use of any third-party libraries (= use only vanilla javascript)

- ✅Implement an interface that follows Bluugo’s brand (https://bluugo.fi/).